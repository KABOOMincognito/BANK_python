def show_balance():
    print("Balance: Rs",balance)



def deposit():
    amount=float(input("Enter amount to deposit:"))
    if (amount<=0):
        print("Enter amount greater than 0")
        return 0
    else:
        return amount



def withdraw():
    amount=float(input("Enter amount to withdraw:"))

    if amount>balance:
        print("Insufficient fund")
        return 0
    elif(amount<=0):
        print("Amount must be greater than 0")
        return 0
    else:
        return amount



balance=0
is_running = True


while is_running:
    print("Banking program")
    print("1.Show balance")
    print("2.Deposit amount")
    print("3.Withdraw amount")
    print("4.Exit")

    choice=input("Enter your choice(1-4):")

    if choice=="1":
        show_balance()
    elif choice=="2":
        balance += deposit()
    elif choice=="3":
        balance -= withdraw()
    elif choice=="4":
        is_running=False
    else:
        print("Wrong choice")

print("Thank You! Have a nice day!")

