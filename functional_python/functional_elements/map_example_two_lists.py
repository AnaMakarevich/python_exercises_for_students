original_price = [10, 20, 25, 34]
taxes = [19, 5, 5, 19]

totals = map(lambda price, tax: price + price * (tax / 100), original_price, taxes)
print(list(totals))
