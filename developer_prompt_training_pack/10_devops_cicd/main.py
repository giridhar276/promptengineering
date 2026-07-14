from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Catalog API")

class Product(BaseModel):
    product_id: str
    name: str
    price: float

PRODUCTS = {
    "P100": Product(product_id="P100", name="Keyboard", price=49.99),
    "P101": Product(product_id="P101", name="Mouse", price=24.99),
}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str):
    return PRODUCTS[product_id]
