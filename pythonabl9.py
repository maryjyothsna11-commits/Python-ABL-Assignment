n = int(input("Number of products: "))
threshold = float(input("Flag changes above (%) : "))

if n <= 0 or threshold < 0:
    print("Invalid product count or threshold.")
else:
    results = []
    valid = True

    for i in range(n):
        name = input(f"Product {i + 1} name: ")
        old_price = float(input("Historical price: "))
        current_price = float(input("Current price: "))

        if old_price <= 0 or current_price < 0:
            print("Invalid price. Restart with valid data.")
            valid = False
            break

        change = (current_price - old_price) / old_price * 100
        if change > 0:
            status = "Increased"
        elif change < 0:
            status = "Decreased"
        else:
            status = "Unchanged"

        results.append((name, change, status))

    if valid:
        for name, change, status in results:
            print(f"{name}: {change:+.2f}% ({status})")
            if abs(change) > threshold:
                print("  Alert: change exceeds threshold.")

        largest = max(results, key=lambda item: abs(item[1]))
        print("Largest fluctuation:", largest[0],
              f"({largest[1]:+.2f}%)")
