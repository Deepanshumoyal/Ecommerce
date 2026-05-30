from fastapi.middleware.cors import CORSMiddleware
from models.order import Order
from schemas.order_schema import OrderCreate
from models.customer import Customer
from schemas.customer_schema import CustomerCreate
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models.product import Product
from schemas.product_schema import ProductCreate
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Backend working with PostgreSQL"}


# CREATE PRODUCT API
@app.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):

    # Check unique SKU
    existing_product = db.query(Product).filter(Product.sku == product.sku).first()

    if existing_product:
        raise HTTPException(status_code=400, detail="SKU already exists")

    new_product = Product(
        name=product.name,
        sku=product.sku,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# GET PRODUCTS API
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
# CREATE CUSTOMER API
@app.post("/customers")
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):

    # Check unique email
    existing_customer = db.query(Customer).filter(Customer.email == customer.email).first()

    if existing_customer:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_customer = Customer(
        name=customer.name,
        email=customer.email
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


# GET CUSTOMERS API
@app.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

# CREATE ORDER API
@app.post("/orders")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):

    # Check customer exists
    customer = db.query(Customer).filter(Customer.id == order.customer_id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Check product exists
    product = db.query(Product).filter(Product.id == order.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Check stock available
    if product.stock < order.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    # Reduce stock
    product.stock -= order.quantity

    # Create order
    new_order = Order(
        customer_id=order.customer_id,
        product_id=order.product_id,
        quantity=order.quantity
    )

    db.add(new_order)

    db.commit()

    db.refresh(new_order)

    return {
        "message": "Order created successfully",
        "remaining_stock": product.stock,
        "order": new_order
    }


# GET ORDERS API
@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

from fastapi.middleware.cors import CORSMiddleware
from models.order import Order
from schemas.order_schema import OrderCreate
from models.customer import Customer
from schemas.customer_schema import CustomerCreate
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, SessionLocal
from models.product import Product
from schemas.product_schema import ProductCreate
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Backend working with PostgreSQL"}


# CREATE PRODUCT API
@app.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):

    # Check unique SKU
    existing_product = db.query(Product).filter(Product.sku == product.sku).first()

    if existing_product:
        raise HTTPException(status_code=400, detail="SKU already exists")

    new_product = Product(
        name=product.name,
        sku=product.sku,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# GET PRODUCTS API
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()
# CREATE CUSTOMER API
@app.post("/customers")
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):

    # Check unique email
    existing_customer = db.query(Customer).filter(Customer.email == customer.email).first()

    if existing_customer:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_customer = Customer(
        name=customer.name,
        email=customer.email
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


# GET CUSTOMERS API
@app.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

# CREATE ORDER API
@app.post("/orders")
def create_order(order: OrderCreate, db: Session = Depends(get_db)):

    # Check customer exists
    customer = db.query(Customer).filter(Customer.id == order.customer_id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Check product exists
    product = db.query(Product).filter(Product.id == order.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Check stock available
    if product.stock < order.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insufficient stock"
        )

    # Reduce stock
    product.stock -= order.quantity

    # Create order
    new_order = Order(
        customer_id=order.customer_id,
        product_id=order.product_id,
        quantity=order.quantity
    )

    db.add(new_order)

    db.commit()

    db.refresh(new_order)

    return {
        "message": "Order created successfully",
        "remaining_stock": product.stock,
        "order": new_order
    }


# GET ORDERS API
# GET ORDERS API
@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):

    orders = db.query(Order).all()
    result = []

    for o in orders:
        customer = db.query(Customer).filter(Customer.id == o.customer_id).first()
        product = db.query(Product).filter(Product.id == o.product_id).first()

        result.append({
            "id": o.id,
            "customer_name": customer.name if customer else "Unknown",
            "product_name": product.name if product else "Unknown",
            "quantity": o.quantity
        })

    return result

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}