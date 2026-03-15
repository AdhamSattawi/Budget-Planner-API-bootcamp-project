#Base class
class Item:
    def __init__(self, name: str, base_price: float, weight: float) -> None:
        self.name = name
        self.base_price = base_price
        self.weight = weight

    def get_info(self) -> str:
        return f"Item name: {self.name}, Price: ${self.base_price}, Weight: {self.weight}Kg"
    

class DiscountMixin:
    def __init__(self, discount_percent: float = 0.0) -> None:
        self.discount_percent = discount_percent

    def get_price(self) -> float:
        base = getattr(self, 'base_price', 0.0)
        discount = (self.discount_percent / 100) * base
        return base - discount
    

class ShippingMixin:
    shipping_rate_per_kg = 5.0 #Dollars per kg

    def get_shipping_cost(self) -> float:
        return self.shipping_rate_per_kg * self.weight


class Product(Item, DiscountMixin, ShippingMixin):
    def __init__(self, name: str, base_price: float, weight: float, discount_percent: float = 0.0) -> None:
        super().__init__(name, base_price, weight)
        self.discount_percent = discount_percent

    def get_info(self) -> str:
        old_info = super().get_info()
        shipping = self.get_shipping_cost()
        return old_info + f", Discount: {self.discount_percent}%, Shipping Price: ${shipping}"
    
    def get_total_cost(self) -> float:
        shipping = self.get_shipping_cost()
        price = self.get_price()
        return price + shipping
    

class DigitalProduct(Item, DiscountMixin):
    def __init__(self, name: str, base_price: float, discount_percent: float = 0.0) -> None:
        super().__init__(name, base_price, weight=0.0)
        self.discount_percent = discount_percent

    def get_info(self):
        return f"Item name: {self.name}, Price: ${self.base_price}, Discount: {self.discount_percent}%"
