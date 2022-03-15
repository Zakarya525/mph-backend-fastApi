from typing import Optional

from pydantic import BaseModel


class AddProductSchema(BaseModel):
    name: str
    description: Optional[str]
    price: Optional[str]


class ProductResponseSchema(BaseModel):
    id: str
    name: str
    description: Optional[str]
    price: str


class ProductUpdateSchema(BaseModel):
    name: str
    description: Optional[str]
    price: str
