from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field


class ReviewBase(BaseModel):
    customer_name: str
    rating: int = Field(ge=1, le=5)
    comment: Optional[str] = None

class ReviewCreate(ReviewBase):
    menu_item_id: int
    customer_id: Optional[int] = None

class ReviewUpdate(BaseModel):
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    comment: Optional[str] = None

class Review(ReviewBase):
    id: int
    menu_item_id: int
    customer_id: Optional[int] = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)