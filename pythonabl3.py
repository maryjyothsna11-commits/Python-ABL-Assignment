width = int(input("Enter an odd width (3 or more): "))

if width < 3 or width % 2 == 0:
    print("Width must be an odd integer of at least 3.")
else:
    middle = width // 2
    for row in range(width):
        distance = row if row <= middle else width - 1 - row
        spaces = middle - distance
        print(" " * spaces, end="")

        if distance == 0:
            print("*")
        else:
            inner_spaces = 2 * distance - 1
            print("*" + " " * inner_spaces + "*")

