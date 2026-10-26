n = int(input("Number of subjects: "))
subjects = []
earlier_scores = []
latest_scores = []

if n <= 0:
    print("Enter at least one subject.")
else:
    valid = True
    for i in range(n):
        subject = input(f"Subject {i + 1} name: ")
        earlier = float(input("Earlier score (0-100): "))
        latest = float(input("Latest score (0-100): "))

        if not (0 <= earlier <= 100 and 0 <= latest <= 100):
            print("Invalid score. Restart the program with valid scores.")
            valid = False
            break

        subjects.append(subject)
        earlier_scores.append(earlier)
        latest_scores.append(latest)

    if valid:
        print("\nPerformance report")
        for i in range(n):
            change = latest_scores[i] - earlier_scores[i]
            if change > 0:
                status = "Improved"
            elif change < 0:
                status = "Declined"
            else:
                status = "Unchanged"
            print(f"{subjects[i]}: {change:+.1f} marks ({status})")

        lowest_index = latest_scores.index(min(latest_scores))
        print("Lowest-scoring subject:", subjects[lowest_index])
