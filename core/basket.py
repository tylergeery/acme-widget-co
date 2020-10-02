from typing import List, Optional

from .checkout import Cart, Chargeable
from .delivery_rule import DeliveryRule
from .product import Product
from .offer import Offer
from query import Queryable



class Basket:
    def __init__(
        self,
        product_catalog: List[Product],
        delivery_rules: List[DeliveryRule],
        offers: List[Offer]
    ):
        self.product_objects = Queryable[Product](product_catalog)
        self.delivery_rule_objects = Queryable[DeliveryRule](delivery_rules)
        self.offer_objects = Queryable[Offer](offers)
        self._basket: List[Product] = []

    @property
    def products(self) -> List[Product]:
        return [product for product in self._basket]

    @property
    def delivery_rules(self) -> List[DeliveryRule]:
        return self.delivery_rule_objects.all()

    @property
    def offers(self) -> List[Offer]:
        return self.offer_objects.all()

    @property
    def charges(self) -> List[Chargeable]:
        # take into account offers before delivery fees
        # These should be ordered
        return self.offers + self.delivery_rules

    def add(self, product_code: str):
        product = self.product_objects.get(code=product_code)
        if not product:
            raise ValueError(f'Unknown product: {product_code}')

        self._basket.append(product)


    def total(self) -> int:
        cart = Cart(self._basket)
        self.cart = cart

        for charge in self.charges:
            cart.total += charge.calculate(cart)

        return cart.total
