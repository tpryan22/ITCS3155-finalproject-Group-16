from sqlalchemy import (
    Column, ForeignKey, Integer, Numeric, UniqueConstraint
)
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    __table_args__ = (
        UniqueConstraint(
            "menu_item_id",
            "ingredient_id",
            name="uq_recipe_menu_item_ingredient"
        ),
    )

    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    menu_item_id = Column(
        Integer,
        ForeignKey("menu_items.id"),
        nullable=False
    )

    ingredient_id = Column(
        Integer,
        ForeignKey("ingredients.id"),
        nullable=False
    )

    quantity_required = Column(
        Numeric(12, 3),
        nullable=False
    )

    menu_item = relationship(
        "MenuItem",
        back_populates="recipes"
    )

    ingredient = relationship(
        "Ingredient",
        back_populates="recipes"
    )