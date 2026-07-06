from sqlalchemy import Column, Integer, String, Float
from database import Base

class Issue(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category = Column(String)
    photo_url = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    status = Column(String, default="Reported")
    upvotes = Column(Integer, default=0)
    rating = Column(Float, default=0.0)