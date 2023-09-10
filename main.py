from fastapi import FastAPI, Query
import datetime

app = FastAPI()

@app.get("/api")
async def read_item(
    slack_name: str = Query(default=None, description="Slack name"),
    track: str = Query(default=None, description="Track")):

    if slack_name is None or track is None:
        return {"error": "Both slack_name and track query parameters are required"}

    now = datetime.datetime.utcnow()
    formatted_utc_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    github_repo_url = "https://github.com/warui09/hng_stage_1"
    github_file_url = github_repo_url + "/blob/main/main.py"
    
    return {
        "slack_name": slack_name,
        "current_day": now.strftime("%A"),
        "utc_time": formatted_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status code": 200
    }
