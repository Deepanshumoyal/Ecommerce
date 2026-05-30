from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    sku: str
    price: int
    stock: int