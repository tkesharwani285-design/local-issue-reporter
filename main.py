from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas import Issue
from database import engine, Base, SessionLocal
import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, Local Issue Reporter is alive!"}

@app.post("/issues")
def create_issue(issue: Issue, db: Session = Depends(get_db)):
    new_issue = models.Issue(
        title=issue.title,
        category=issue.category,
        photo_url=issue.photo_url,
        latitude=issue.latitude,
        longitude=issue.longitude,
        status=issue.status,
        upvotes=issue.upvotes,
        rating=issue.rating
    )
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue

@app.get("/issues")
def get_issues(db: Session = Depends(get_db)):
    return db.query(models.Issue).all()