from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Category(Base):
    __tablename__ = "categories"

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

    menu_items = relationship(
        "MenuItem",
        back_populates="category"
    )