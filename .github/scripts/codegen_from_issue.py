import os
import openai
from github import Github
from datetime import datetime

# Check API keys
openai_key = os.getenv("OPENAI_API_KEY")
github_token = os.getenv("GITHUB_TOKEN")
repo_name = os.getenv("GITHUB_REPOSITORY")

if not openai_key or not github_token or not repo_name:
    raise RuntimeError("Missing required environment variables.")

# Set keys
openai.api_key = openai_key
gh = Github(github_token)

# Load repo and issue
repo = gh.get_repo(repo_name)
issues = repo.get_issues(state='open', labels=[repo.get_label("codegen")])

if issues.totalCount == 0:
    print("No open issues with 'codegen' label.")
    exit(0)

# Use first matching issue
issue = issues[0]
print(f"Using issue #{issue.number}: {issue.title}")

# Prompt construction
prompt = f"""
Generate Python code based on the following GitHub issue.

Title: {issue.title}

Description:
{issue.body}

Requirements:
- Follow Python best practices
- Include input validation
- Add at least one test case
"""

try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a senior Python developer."},
            {"role": "user", "content": prompt}
        ]
    )
except Exception as e:
    print(f"OpenAI API error: {e}")
    exit(1)

code = response['choices'][0]['message']['content']
filename = f"generated_{issue.number}.py"

with open(filename, "w") as f:
    f.write(code)

# Create new branch
branch_name = f"codegen/{issue.number}-{issue.title.lower().replace(' ', '-')[:30]}"
source_sha = repo.get_branch("main").commit.sha
repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=source_sha)
print(f"Created branch {branch_name}")

# Commit file
repo.create_file(
    path=filename,
    message=f"Auto-generated code for issue #{issue.number}",
    content=code,
    branch=branch_name
)
print(f"Committed code to {branch_name}")

# Open PR
repo.create_pull(
    title=f"[Auto-CodeGen] {issue.title}",
    body=f"This PR was auto-generated from issue #{issue.number}.",
    head=branch_name,
    base="main"
)
print("Pull request created.")

