from core import Basket, DeliveryRule, Offer, Product, DeliveryTier
from core.offer import TwoForOneOffer


optional_baskets = [
    ('B01', 'G01'),
    ('R01', 'R01'),
    ('R01', 'G01'),
    ('B01', 'B01', 'R01', 'R01', 'R01'),
]


class BasketBuilderCLI:
    def __init__(self, basket: Basket):
        self.basket: Basket = basket

    @staticmethod
    def _curr(amount: int) -> str:
        return f'${amount/100:,.2f}'

    def _product(self, product: Product):
        return f'{product.name}: {self._curr(product.price)}'

    def _offer(self, offer: Offer):
        return f'Offer: {self._curr(offer.calculate(self.basket.cart))}'

    def _delivery(self, rule: DeliveryRule):
        return f'Delivery: {self._curr(rule.calculate(self.basket.cart))}'

    def run(self):

        prompt = 'Please input all the basket items for evaluation\n\nSelect from the following list of options by number, or input all product codes in CSV format:\n'
        for i, product_codes in enumerate(optional_baskets):
            prompt += f'\t{i}: {optional_baskets[i]}\n'
        val = input(prompt)

        if val.isdigit():
            try:
                items = optional_baskets[int(val)]
            except IndexError:
                return self.run()
        else:
            items = [product_code.strip() for product_code in val.split(',') if product_code]

        if not items:
            return self.run()

        for item in items:
            self.basket.add(item)
        self.basket.total()

    def summarize(self):
        line_items = [self._product(product) for product in self.basket.products]
        line_items += [self._offer(offer) for offer in self.basket.offers]
        line_items += [self._delivery(rule) for rule in self.basket.delivery_rules]
        line_items.append(f'Total: {self._curr(self.basket.total())}')

        print('\n'.join(line_items))


if __name__ == '__main__':
    product_catalog = [
        Product('Red Widget', 'R01', 3295),
        Product('Green Widget', 'G01', 2495),
        Product('Blue Widget', 'B01', 795),
    ]
    delivery_rules = [
        DeliveryRule(
            [
                DeliveryTier(5000, 495),
                DeliveryTier(9000, 295),
                DeliveryTier(0, 0)
            ]
        )
    ]
    offers = [
        TwoForOneOffer('R01'),
    ]

    basket = Basket(product_catalog, delivery_rules, offers)
    basket_builder = BasketBuilderCLI(basket)
    basket_builder.run()
    basket_builder.summarize()
