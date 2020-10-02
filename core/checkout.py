import abc
from typing import List

from .product import Product


class Cart:
    def __init__(self, products: List[Product]):
        self.products = products
        self.total = sum(product.price for product in products)


class Chargeable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self, cart: Cart) -> int:
        pass

