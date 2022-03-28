from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from database import get_db_session
from models import Product, User
from schemas.product import AddProductSchema, ProductResponseSchema, ProductUpdateSchema
from utils import get_current_user, verify_token

product_router = APIRouter(prefix="/products", tags=['Products'])


@product_router.get("/{product_id}", response_model=ProductResponseSchema)
def get_product(product_id: str, current_user: User = Depends(get_current_user)):
    with get_db_session() as db_session:
        product: Product = db_session.get(Product, product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product '{product_id}' cannot be found.",
            )
        return product.to_json()


@product_router.post("", response_model=ProductResponseSchema)
def create_product(product_data: AddProductSchema, username: User = Depends(verify_token)):
    with get_db_session() as db_session:
        user = db_session.query(User).filter_by(user_name=username).first()
        if not user.store:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User '{user.user_name}' no store created yet. Please create one..",
            )

        existing_product = db_session.query(Product).filter_by(price=product_data.price,
                                                               description=product_data.description,
                                                               name=product_data.name).first()
        if existing_product:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User '{user.user_name}' has already one product created.",
            )
        product = Product(**product_data.dict())
        product.user = user
        product.store = user.store
        db_session.add(product)
        db_session.commit()

        return product.to_json()


@product_router.delete("/{product_id}", status_code=202)
def delete_product(product_id: str, current_user: User = Depends(get_current_user)):
    with get_db_session() as db_session:
        product: Product = db_session.get(Product, product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product '{product_id}' cannot be found.",
            )
        db_session.delete(product)
        db_session.commit()

        return product.to_json()


@product_router.patch("/{product_id}")
def update_product(product_id: str, update_product_data: ProductUpdateSchema,
                   current_user: User = Depends(get_current_user)):
    with get_db_session() as db_session:
        product: Product = db_session.get(Product, product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product '{product_id}' cannot be found.",
            )

        product.description = update_product_data.description
        db_session.commit()

        return product.to_json()
