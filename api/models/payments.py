from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Enum
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from .enums import PaymentMethod, PaymentStatus


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False, unique=True)
    saved_payment_method_id = Column(Integer, ForeignKey("saved_payment_methods.id"), nullable=True)
    method = Column(Enum(PaymentMethod), nullable=False)
    status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.pending)
    amount = Column(DECIMAL(10, 2), nullable=False)
    card_last_four = Column(String(4), nullable=True)
    paid_at = Column(DATETIME, nullable=True)

    order = relationship("Order", back_populates="payment")
    saved_payment_method = relationship("SavedPaymentMethod", back_populates="payments")
