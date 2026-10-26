balance = float(input("Enter opening balance: "))
n = int(input("Enter number of transactions: "))

deposits = 0
withdrawals = 0
rejected = 0

if balance < 0 or n < 0:
    print("Invalid opening balance or transaction count.")
else:
    for i in range(n):
        print("\nTransaction", i + 1)
        transaction_type = input("Enter D for deposit or W for withdrawal: ").upper()
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Invalid amount.")
            rejected += 1
        elif transaction_type == "D":
            balance += amount
            deposits += 1
            print("Deposit successful.")
        elif transaction_type == "W":
            if amount <= balance:
                balance -= amount
                withdrawals += 1
                print("Withdrawal successful.")
            else:
                print("Insufficient balance. Transaction rejected.")
                rejected += 1
        else:
            print("Invalid transaction type.")
            rejected += 1

    print("\n--- ATM Transaction Summary ---")
    print(f"Final balance: Rs. {balance:.2f}")
    print("Successful deposits:", deposits)
    print("Successful withdrawals:", withdrawals)
    print("Rejected transactions:", rejected)
