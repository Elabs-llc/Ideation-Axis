products = [
    {"name": "Laptop", "stock": 5, "price": 1500},
    {"name": "Smartphone", "stock": 0, "price": 700},
    {"name": "Tablet", "stock": 10, "price": 400},
    {"name": "Television", "stock": 5, "price": 1900},
    {"name": "Fridge", "stock": 6, "price": 1700},
    {"name": "Speaker", "stock": 15, "price": 200},
]

# List comprehension to get in-stock product names in lowercase
in_stock_products = [product['name'].lower() for product in products if product['stock'] > 0]

print('Products available in stock: ')
print('==============================')
print(in_stock_products)
