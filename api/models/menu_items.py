from sqlalchemy import (
    Boolean, Column, ForeignKey, Integer, Numeric, String
)
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )

    name = Column(String(100), nullable=False)

    description = Column(String(500), nullable=True)

    price = Column(Numeric(10, 2), nullable=False)

    calories = Column(Integer, nullable=True)

    is_active = Column(Boolean, nullable=False, default=True)

    category = relationship(
        "Category",
        back_populates="menu_items"
    )

    recipes = relationship(
        "Recipe",
        back_populates="menu_item"
    )

    order_items = relationship(
        "OrderItem",
        back_populates="menu_item"
    )

    reviews = relationship(
        "Review",
        back_populates="menu_item"
    )