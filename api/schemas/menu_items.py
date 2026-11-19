from decimal import Decimal
from pydantic import BaseModel, ConfigDict, Field


class MenuItemBase(BaseModel):
    category_id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=100)
    description: str | None = None
    price: Decimal = Field(gt=0)
    calories: int | None = Field(default=None, ge=0)
    is_active: bool = True


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(BaseModel):
    category_id: int | None = Field(default=None, gt=0)
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )
    description: str | None = None
    price: Decimal | None = Field(default=None, gt=0)
    calories: int | None = Field(default=None, ge=0)
    is_active: bool | None = None


class MenuItem(MenuItemBase):
    id: int

    model_config = ConfigDict(from_attributes=True)