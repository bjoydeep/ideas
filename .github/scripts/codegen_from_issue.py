import os
from github import Github
from openai import OpenAI

# === Load environment variables ===
openai_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("GITHUB_TOKEN")
repo_name = os.getenv("GITHUB_REPOSITORY")

if not all([openai_key, github_token, repo_name]):
    raise RuntimeError("Missing required environment variables.")

# === Init clients ===
client = OpenAI(api_key=openai_key)
gh = Github(github_token)
repo = gh.get_repo(repo_name)

# === Get most recently updated issue with label 'codegen' ===
issues = sorted(
    repo.get_issues(state='open', labels=["codegen"]),
    key=lambda i: i.updated_at,
    reverse=True
)

if not issues:
    print("No open issues with 'codegen' label.")
    exit(0)

issue = issues[0]
issue_number = issue.number
issue_title = issue.title
issue_body = issue.body or ""
print(f"Using issue #{issue_number}: {issue_title}")

# === Generate code with OpenAI ===
prompt = f"""
Generate Python code based on the following GitHub issue.

Title: {issue_title}

Description:
{issue_body}

Requirements:
- Follow Python best practices
- Include input validation
- Add at least one test case
"""

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a senior Python developer."},
        {"role": "user", "content": prompt}
    ]
)

code = response.choices[0].message.content
filename = f"generated_{issue_number}.py"
branch_name = f"codegen/{issue_number}-{issue_title.lower().replace(' ', '-')[:30]}"

# === Create or reuse branch ===
try:
    repo.get_branch(branch_name)
    print(f"Branch {branch_name} already exists.")
except:
    source_sha = repo.get_branch("main").commit.sha
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=source_sha)
    print(f"Created branch {branch_name}")

# === Create or update file ===
try:
    contents = repo.get_contents(filename, ref=branch_name)
    repo.update_file(
        path=filename,
        message=f"♻️ Regenerated code for issue #{issue_number}",
        content=code,
        sha=contents.sha,
        branch=branch_name
    )
    print(f"✅ Updated file {filename} on branch {branch_name}")
except:
    repo.create_file(
        path=filename,
        message=f"✨ Auto-generated code for issue #{issue_number}",
        content=code,
        branch=branch_name
    )
    print(f"✅ Created new file {filename} on branch {branch_name}")

# === Create PR only if not already created ===
existing_prs = repo.get_pulls(state="open", head=f"{repo.owner.login}:{branch_name}")
if existing_prs.totalCount == 0:
    pr = repo.create_pull(
        title=f"[Auto-CodeGen] {issue_title}",
        body=f"This PR was auto-generated from issue #{issue_number}.",
        head=branch_name,
        base="main"
    )
    print(f"📬 Pull request created: #{pr.number}")
else:
    print("PR already exists for this branch.")
