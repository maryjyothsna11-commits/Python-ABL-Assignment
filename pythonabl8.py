days = int(input("Number of days: "))
limit = float(input("Acceptable waste percentage: "))

if days <= 0 or not 0 <= limit <= 100:
    print("Invalid number of days or waste limit.")
else:
    records = []
    valid = True

    for day in range(1, days + 1):
        prepared = int(input(f"Day {day} meals prepared: "))
        served = int(input(f"Day {day} meals served: "))

        if prepared <= 0 or served < 0 or served > prepared:
            print("Invalid quantities. Restart with valid data.")
            valid = False
            break

        leftovers = prepared - served
        waste = leftovers / prepared * 100
        records.append((day, prepared, served, leftovers, waste))

    if valid:
        for day, prepared, served, leftovers, waste in records:
            print(f"Day {day}: leftovers={leftovers}, waste={waste:.2f}%")
            if waste > limit:
                print("  Warning: waste exceeds the acceptable limit.")

        highest = max(records, key=lambda record: record[4])
        print("Highest waste percentage:", f"{highest[4]:.2f}%")
        print("Day with highest waste:", highest[0])
