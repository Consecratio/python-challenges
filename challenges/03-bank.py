print("Welcome to Chase bank.")
bal = 4000

def balance():
    print("Your current balance is\n", bal)

def withdraw():
    global bal
    num = input("How much would you like to withdraw?\n")
    bal -= int(num)
    print(f"Your new balance is\n{bal}")

def deposit():
    global bal
    num = input("How much would you like to deposit?\n")
    bal += int(num)
    print(f"Your new balance is\n{bal}")

cust_choice = input("What would you like to do? (deposit, withdraw, check_balance)\n")

if cust_choice == "deposit":
    deposit()    

if cust_choice == "withdraw":
    withdraw()

if cust_choice == "check_balance":
    balance()

print("Have a nice day!")

