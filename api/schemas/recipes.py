from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class RecipeBase(BaseModel):
    quantity_required: Decimal = Field(gt=0)


class RecipeCreate(RecipeBase):
    menu_item_id: int = Field(gt=0)
    ingredient_id: int = Field(gt=0)


class RecipeUpdate(BaseModel):
    menu_item_id: int | None = Field(default=None, gt=0)
    ingredient_id: int | None = Field(default=None, gt=0)

    quantity_required: Decimal | None = Field(
        default=None,
        gt=0
    )


class Recipe(RecipeBase):
    id: int
    menu_item_id: int
    ingredient_id: int

    model_config = ConfigDict(from_attributes=True)