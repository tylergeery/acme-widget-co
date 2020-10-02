# acme-widget-co
A Basket interface and CLI to checkout and calculate ACME widgets

## Assumptions
- No such thing as a half penny
- Offers should be calculated before delivery charges

## Run instructions
```bash
python3 main.py
```

Follow the prompt to either input one of the popular available baskets or create your own (e.g R01, G01, B01)

## Example
```
Please input all the basket items for evaluation

Select from the following list of options by number, or input all product codes in CSV format:
	0: ('B01', 'G01')
	1: ('R01', 'R01')
	2: ('R01', 'G01')
	3: ('B01', 'B01', 'R01', 'R01', 'R01')
2
Red Widget: $32.95
Green Widget: $24.95
Offer: $0.00
Delivery: $2.95
Total: $60.85
```

### TODO:
- Add tests
- Limit CLI from outputting all lines (e.g if offer not used)
- Aggregate CLI output for each product type (e.g Red Widget (x2))
- create a DSL for offers
  - e.g (count(R01) / 2 ) * (RO1.price/2)