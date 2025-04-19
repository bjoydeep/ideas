import os, json, sys
from github import Github
from openai import OpenAI

# Load the event payload
event_path = os.environ.get("GITHUB_EVENT_PATH")
if not event_path or not os.path.exists(event_path):
    print("ERROR: GITHUB_EVENT_PATH not set or invalid", file=sys.stderr)
    sys.exit(1)

with open(event_path) as f:
    data = json.load(f)

# 1) Direct pull_request webhook (pull_request trigger)
if "pull_request" in data:
    pr_number = data["pull_request"]["number"]

# 2) workflow_run webhook (workflow_run trigger)
elif "workflow_run" in data and data["workflow_run"].get("pull_requests"):
    prs = data["workflow_run"]["pull_requests"]
    # pick the first associated PR
    pr_number = prs[0]["number"]

# 3) Fallback: search by branch name
else:
    branch = data.get("workflow_run", {}).get("head_branch")
    if not branch:
        print("ERROR: Cannot determine PR number or branch", file=sys.stderr)
        sys.exit(1)
    # repo is something like "owner/name"
    repo = Github(os.environ["GITHUB_TOKEN"]) \
               .get_repo(os.environ["GITHUB_REPOSITORY"])
    matches = repo.get_pulls(head=f"{repo.owner.login}:{branch}", state="open")
    if matches.totalCount == 0:
        print(f"ERROR: No open PR found for branch {branch}", file=sys.stderr)
        sys.exit(1)
    pr_number = matches[0].number

# Environment & context
gh = Github(os.environ["GITHUB_TOKEN"])
repo = gh.get_repo(os.environ["GITHUB_REPOSITORY"])
#pr_number = int(os.environ["GITHUB_REF"].split("/")[-1])
pr = repo.get_pull(pr_number)

openai_key = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_key)

# Gather changed files & diffs
files = pr.get_files()
comments = []

for f in files:
    # Only review .py files, or whatever you like
    if not f.filename.endswith(".py"):
        continue

    diff = f.patch
    if not diff:
        continue

    # Send the diff to OpenAI for review
    #resp = openai.ChatCompletion.create(
    resp = client.chat.completions.create(    
        model="gpt-4o-mini",
        messages=[
          {"role": "system", "content": "You are a code review assistant."},
          {"role": "user",   "content": f"Please review this patch and suggest improvements:\n\n```diff\n{diff}\n```"}
        ]
    )
    review_text = resp.choices[0].message.content.strip()

    # Post as a PR review comment
    pr.create_review(
        body=review_text,
        event="COMMENT"
    )

print(f"Posted review on PR #{pr_number}")
