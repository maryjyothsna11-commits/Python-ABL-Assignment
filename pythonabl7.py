products = [
    ("P101", 25.50, 10),
    ("P102", 120.00, 3),
    ("P103", 45.00, 0)
]

total_value = 0

print("Product Catalogue Audit")
for product in products:
    product_id, price, quantity = product

    if price < 0 or quantity < 0:
        print(product_id, "has an invalid record.")
    else:
        value = price * quantity
        total_value += value
        print(f"{product_id}: stock value = Rs. {value:.2f}")
        if quantity < 5:
            print("  Replenishment required.")

print(f"Total inventory value: Rs. {total_value:.2f}")
