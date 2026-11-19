from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from ..models.enums import PaymentMethod, PaymentStatus


class PaymentBase(BaseModel):
    method: PaymentMethod
    amount: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    card_last_four: Optional[str] = Field(default=None, min_length=4, max_length=4)


class PaymentCreate(PaymentBase):
    order_id: int
    saved_payment_method_id: Optional[int] = None


class PaymentUpdate(BaseModel):
    status: Optional[PaymentStatus] = None
    paid_at: Optional[datetime] = None


class Payment(PaymentBase):
    id: int
    order_id: int
    saved_payment_method_id: Optional[int] = None
    status: PaymentStatus
    paid_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)
