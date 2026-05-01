from pydantic import BaseModel

class OrderRequest(BaseModel):
    text: str

class OrderResponse(BaseModel):
    dish: str
    no_onion: bool
    spicy_level: str