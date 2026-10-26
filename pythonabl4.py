password = input("Enter a sample password: ")

failures = []
if len(password) < 8:
    failures.append("Use at least 8 characters.")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True

if not has_upper:
    failures.append("Include an uppercase letter.")
if not has_lower:
    failures.append("Include a lowercase letter.")
if not has_digit:
    failures.append("Include a digit.")
if not has_special:
    failures.append("Include a special character.")

if len(failures) == 0:
    print("Password meets the classroom policy.")
else:
    print("Password does not meet the policy:")
    for rule in failures:
        print("-", rule)
