conducted = int(input("Classes conducted: "))
attended = int(input("Classes attended: "))
required = float(input("Required attendance percentage: "))

if (conducted <= 0 or attended < 0 or attended > conducted
        or required < 0 or required > 100):
    print("Invalid input")
else:
    current = attended / conducted * 100
    print(f"Current attendance: {current:.2f}%")

    additional = 0
    while current < required:
        attended += 1
        conducted += 1
        additional += 1
        current = attended / conducted * 100

    if additional == 0:
        print("You already meet the attendance requirement.")
    else:
        print("Additional consecutive classes required:", additional)
    print(f"Attendance after recovery: {current:.2f}%")
