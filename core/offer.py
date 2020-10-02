import math
from collections import defaultdict
from .checkout import Cart, Chargeable


class Offer(Chargeable):
    pass


class TwoForOneOffer(Offer):
    def __init__(self, product_code: str):
        self.product_code = product_code

    @staticmethod
    def agg_products(cart: Cart):
        aggs = defaultdict(list)

        for product in cart.products:
            aggs[product.code].append(product)

        return aggs

    def calculate(self, cart: Cart) -> int:
        # TODO: remove this from being hardcoded
        # ideally create a DSL to easily represent arbitrary offers
        aggs = self.agg_products(cart)
        product_count = len(aggs[self.product_code])

        if not product_count:
            return 0

        return -1 * int(product_count / 2) * math.ceil(aggs[self.product_code][0].price/2)