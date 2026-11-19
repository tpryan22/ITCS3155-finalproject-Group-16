from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class IngredientBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)

    stock_quantity: Decimal = Field(
        default=Decimal("0"),
        ge=0
    )

    unit: str = Field(min_length=1, max_length=30)

    low_stock_threshold: Decimal = Field(
        default=Decimal("0"),
        ge=0
    )


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    stock_quantity: Decimal | None = Field(
        default=None,
        ge=0
    )

    unit: str | None = Field(
        default=None,
        min_length=1,
        max_length=30
    )

    low_stock_threshold: Decimal | None = Field(
        default=None,
        ge=0
    )


class Ingredient(IngredientBase):
    id: int

    model_config = ConfigDict(from_attributes=True)