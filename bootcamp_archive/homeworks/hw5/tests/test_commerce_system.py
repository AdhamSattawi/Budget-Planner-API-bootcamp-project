import pytest
from solution.ecommerce_system import Product



def test_product():
    laptop = Product("Laptop", 1000.0, 2.5, discount_percent=10)
    assert laptop.get_price() == 900.0
    assert laptop.get_shipping_cost() == 12.5
    assert laptop.get_total_cost() == 912.5
    assert laptop.get_info() == "Item name: Laptop, Price: $1000.0, Weight: 2.5Kg, Discount: 10%, Shipping Price: $12.5"

    