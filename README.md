# acme-widget-co
A Basket interface and CLI to checkout and calculate ACME widgets

## Assumptions
- No such thing as a half penny
- Offers should be calculated before delivery charges (more revenue)

## Run instructions
```bash
python3 main.py
```

Follow the prompt to either input one of the popular available baskets or create your own

## TODO:
- Add tests
- Limit CLI from outputting all lines (e.g if offer not used)
- create a DSL for offers
  - e.g (count(R01) / 2 ) * (RO1.price/2)