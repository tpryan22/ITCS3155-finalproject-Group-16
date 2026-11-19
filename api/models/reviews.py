from sqlalchemy import Column, ForeignKey, Integer, String, DATETIME, func, CheckConstraint
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"
    __table_args__ = (CheckConstraint("rating BETWEEN 1 AND 5"),)
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    customer_name = Column(String(100), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(500), nullable=True)
    created_at = Column(DATETIME, nullable=False, server_default=func.now())

    menu_item = relationship("MenuItem", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")