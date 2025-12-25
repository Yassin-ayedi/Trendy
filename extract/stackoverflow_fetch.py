import requests
import pandas as pd
import logging
from datetime import datetime
from utils import upload_to_datalake
from tqdm import tqdm

def fetch_stackoverflow():
    tags = [
        "data-analysis", "data-science", "data-engineering",
        "business-analysis", "machine-learning",
        "programming", "cloud-computing"
    ]

    rows = []

    for tag in tqdm(tags):
        url = "https://api.stackexchange.com/2.3/questions"
        params = {
            "tagged": tag,
            "pagesize": 100,
            "order": "desc",
            "sort": "activity",
            "site": "stackoverflow",
            "filter": "withbody"
        }

        logging.info(f"🔍 Fetching StackOverflow questions for tag: {tag}")
        response = requests.get(url, params=params)
        data = response.json()

        for item in data.get("items", []):
            rows.append({
                "title": item["title"],
                "body": item["body"],
                "tools": item["tags"],
                "date": item["creation_date"],
                "score": item["score"],
                "answer_count": item["answer_count"],
                "favorite_count": item.get("favorite_count", 0),
                "view_count": item["view_count"],
                "is_answered": item["is_answered"],
                "job": tag
            })


    tag_to_job = {"programming": "Software Engineer"}
    df = pd.DataFrame(rows)
    df["job"] = df["job"].map(tag_to_job).fillna(df["job"])


    timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"stackoverflow_questions_{timestamp}.json"
    json_data = df.to_json(orient="records", indent=2)

    # Upload to Data Lake (bronze)
    upload_to_datalake(json_data, file_name, filesystem_name="bronze/stackoverflow")
