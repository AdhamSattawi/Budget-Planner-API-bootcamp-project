from fastapi import FastAPI    
from product_service import ProductsService
from product import Product

app = FastAPI()
PRODUCT_SERVICES = ProductsService()

@app.get("/products")
async def get_products() -> list[Product]:
    return PRODUCT_SERVICES.get_all_products()

@app.get("/products/{product_id}") 
async def get_product_id(product_id: int) -> Product: 
    return PRODUCT_SERVICES.get_product_by_id(product_id)

@app.post("/products")
async def new_product(new_product: Product):
    PRODUCT_SERVICES.create_product(new_product)
    return {"status":"success", "added": new_product}