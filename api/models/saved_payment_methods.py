from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class SavedPaymentMethod(Base):
    __tablename__ = "saved_payment_methods"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    card_brand = Column(String(50), nullable=False)
    card_last_four = Column(String(4), nullable=False)
    expiration = Column(String(5), nullable=False)
    is_default = Column(Boolean, nullable=False, default=False)

    customer = relationship("Customer", back_populates="saved_payment_methods")
    payments = relationship("Payment", back_populates="saved_payment_method")