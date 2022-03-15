from typing import Optional

from pydantic import BaseModel

from schemas.product import ProductResponseSchema


class CreateStoreSchema(BaseModel):
    title: str
    description: Optional[str]


class StoreResponseSchema(BaseModel):
    id: str
    title: str
    description: Optional[str]
    products: [ProductResponseSchema]


class StoreUpdateSchema(BaseModel):
    description: str
