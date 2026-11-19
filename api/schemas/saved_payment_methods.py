from typing import Optional
from pydantic import BaseModel
from pydantic import ConfigDict


class SavedPaymentMethodBase(BaseModel):
    card_brand: str
    card_last_four: str
    expiration: str
    is_default: bool = False

class SavedPaymentMethodCreate(SavedPaymentMethodBase):
    customer_id: int

class SavedPaymentMethod(SavedPaymentMethodBase):
    id: int
    customer_id: int
    model_config = ConfigDict(from_attributes=True)


class SavedPaymentMethodUpdate(BaseModel):
    card_brand: Optional[str] = None
    card_last_four: Optional[str] = None
    expiration: Optional[str] = None
    is_default: Optional[bool] = None