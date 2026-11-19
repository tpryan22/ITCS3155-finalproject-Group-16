from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    name = Column(
        String(100),
        nullable=False,
        unique=True
    )

    stock_quantity = Column(
        Numeric(12, 3),
        nullable=False,
        default=0
    )

    unit = Column(String(30), nullable=False)

    low_stock_threshold = Column(
        Numeric(12, 3),
        nullable=False,
        default=0
    )

    recipes = relationship(
        "Recipe",
        back_populates="ingredient"
    )