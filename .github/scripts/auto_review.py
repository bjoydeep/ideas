import os, json, sys
from github import Github
import openai

# load event JSON
event_path = os.environ.get("GITHUB_EVENT_PATH")
if not event_path or not os.path.exists(event_path):
    print("ERROR: GITHUB_EVENT_PATH not set or invalid", file=sys.stderr)
    sys.exit(1)

with open(event_path) as f:
    data = json.load(f)
pr_number = data["pull_request"]["number"]

# Environment & context
gh = Github(os.environ["GITHUB_TOKEN"])
repo = gh.get_repo(os.environ["GITHUB_REPOSITORY"])
#pr_number = int(os.environ["GITHUB_REF"].split("/")[-1])
pr = repo.get_pull(pr_number)

openai.api_key = os.environ["OPENAI_API_KEY"]

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
    resp = openai.ChatCompletion.create(
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
