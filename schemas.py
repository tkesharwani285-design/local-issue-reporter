from pydantic import BaseModel

class Issue(BaseModel):
    title: str
    category: str
    photo_url: str
    latitude: float
    longitude: float
    status: str = "Reported"
    upvotes: int = 0
    rating: float = 0.0