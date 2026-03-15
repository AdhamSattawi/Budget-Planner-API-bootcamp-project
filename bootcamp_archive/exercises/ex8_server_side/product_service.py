from product import Product
import json

with open("products.json", "r") as file:
    PRODUCTS_LIST = json.load(file)

class ProductsService:
    def get_all_products(self) -> list[Product]:
        return [Product(**product) for product in PRODUCTS_LIST]
    
    def get_product_by_id(self, product_id: int) -> Product:
        for product in PRODUCTS_LIST:
            if product["id"] == product_id:
                return product
        raise ValueError("not found!")
    
    def create_product(self, name: str, description: str, price: float, stock: int) -> Product:
        new_id = PRODUCTS_LIST[-1]["id"] + 1
        new_product = {
            "id" : new_id,
            "name":name, 
            "description": description,
            "price": price,
            "stock": stock
            }
        PRODUCTS_LIST.append(new_product)
        return Product(**new_product)
