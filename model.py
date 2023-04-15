from pydantic import BaseModel


class Quote(BaseModel):
    id: int
    autor: str
    content: str
    leader: str
    leader_image: str
    reference: str
