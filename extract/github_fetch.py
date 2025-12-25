import requests
import time
import base64
import pandas as pd
from datetime import datetime
import os
import logging
from utils import upload_to_datalake
import json
from tqdm import tqdm

GITHUB_BLACKLIST = {
    "github", "git", "bash", "shell", "sh",
    "html", "css", "windows", "flow"
}

def get_readme(owner, repo, headers):
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return ""
    data = resp.json()
    content = data.get("content", "")
    try:
        return base64.b64decode(content).decode("utf-8", errors="ignore")
    except:
        return ""

def fetch_github():
    github_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
    if not github_token:
        logging.error("❌ Missing GitHub token!")
        return

    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {github_token}"
    }

    jobs = [
        "Data Analyst",
        "Data Engineer",
        "Business Analyst",
        "Data Scientist",
        "Machine Learning Engineer",
        "Cloud Engineer",
        "Software Engineer"
    ]

    rows = []

    for job in tqdm(jobs):
        logging.info(f"Searching GitHub for: {job}")

        query = f"{job} in:readme in:description"
        url = "https://api.github.com/search/repositories"
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc",
            "per_page": 20
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        repos = data.get("items", [])

        for repo in repos:
            full_name = repo["full_name"]
            owner, name = full_name.split("/")
            readme_text = get_readme(owner, name, headers)

            rows.append({
                "job": job,
                "url": repo["html_url"],
                "description": repo.get("description", ""),
                "created_at": repo["created_at"],
                "stars": repo.get("stargazers_count"),
                "forks": repo.get("forks_count"),
                "watchers": repo.get("watchers_count"),
                "readme": readme_text[:10000],
                #"readme_2": readme_text[100000:200000],
                "topics": repo.get("topics", []),
                "language": repo.get("language")
            })

        time.sleep(1)


    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"github_repos_{timestamp}.json"
    json_data = json.dumps(rows, ensure_ascii=False)



    upload_to_datalake(json_data, file_name, filesystem_name="bronze/github")
        
