from typing import List

from .checkout import Cart, Chargeable


class DeliveryTier:
    def __init__(self, max: int, charge: int):
        self.max = max
        self.charge = charge


class DeliveryRule(Chargeable):
    def __init__(self, ordered_tiers: List[DeliveryTier]):
        self.ordered_tiers = ordered_tiers

    def calculate(self, cart: Cart) -> int:
        if not self.ordered_tiers:
            return 0

        if not cart.products:
            return 0

        for tier in self.ordered_tiers:
            if tier.max > cart.total:
                return tier.charge

        return self.ordered_tiers[-1].charge
