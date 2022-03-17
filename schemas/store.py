from typing import List, Optional

from pydantic import BaseModel

from schemas.product import ProductResponseSchema, ProductUpdateSchema


class CreateStoreSchema(BaseModel):
    title: str
    description: Optional[str]


class StoreResponseSchema(BaseModel):
    id: str
    title: str
    description: Optional[str]
    products: List[ProductResponseSchema]


class StoreUpdateSchema(BaseModel):
    description: str
    products: Optional[List[ProductUpdateSchema]]
