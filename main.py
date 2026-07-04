from fastapi import FastAPI
from schemas import Issue

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Local Issue Reporter is alive!"}

@app.post("/issues")
def create_issue(issue: Issue):
    return {"message": "Issue received successfully", "data": issue}