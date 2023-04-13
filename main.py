import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/repos/{username}")
def get_repos(username: str):
    url = "http://localhost:5000/repos/{}".format(username)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"message": "Error fetching data from Flask app"}
