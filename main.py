# Programmers:  Jalen, Cameron
# Course:  CS151, professor zee
# Due Date: oct 24, 2024
# Programming Assignment:  lab 6
# Problem Statement:  You need to refactor the ATM application so that it has proper error checking and functions
# Data In: choice, withdraw amount, deposit, amount
# Data Out:  balance, errors with negative deposit and withdraw,
# Credits: professor zee, lab 5 solution
# Display the purpose of the program


def display_choice():
    print("\nPlease select an option:"
          "\n\t D - Deposit"
          "\n\t W - Withdraw"
          "\n\t V - View Balance"
          "\n\t E - Exit")
    return input("Your choice: ").strip().upper()

def deposit(current_balance):
    deposit_amount = input("Enter the amount to deposit: ").strip()
    if deposit_amount.isdigit():
        deposit_amount = int(deposit_amount)
        if deposit_amount < 0:
            print("Error: Please enter a positive number.")
        else:
            current_balance += deposit_amount
            print(f"Deposit successful! Your new balance is ${current_balance:.2f}.")
    else:
        print("Error: Please enter a valid number.")
    return current_balance

def withdraw(current_balance):
    withdraw_amount = input("Enter the amount to withdraw: ").strip()
    if withdraw_amount.isdigit():
        withdraw_amount = int(withdraw_amount)
        if withdraw_amount < 0:
            print("Error: Please enter a positive number.")
        else:
            current_balance -= withdraw_amount
            print(f"Withdrawal successful! Your new balance is ${current_balance:.2f}.")

            # Warning if the balance is negative
            if current_balance < 0:
                print("❕ Warning: You have a negative balance. You will be charged 5% interest.")
    else:
        print("Error: Please enter a valid number.")
    return current_balance

def view(current_balance):
    print(f"Your current balance is ${current_balance:.2f}.")
    return

def main():
    print("Welcome to the ATM program! This program allows you to interact with your account balance.")
    # Initialize variables
    INITIAL_BALANCE = 1000
    current_balance = INITIAL_BALANCE
    SENTINEL = 'E'
    choice = ''
    while choice .upper() != SENTINEL:
        choice = display_choice()
        if choice == 'D':
            current_balance = deposit(current_balance)
        elif choice == 'W':
            current_balance = withdraw(current_balance)
        elif choice == 'V':
            current_balance = view(current_balance)
        elif choice == 'E':
            print("Thank you for using the ATM program. Goodbye!")
        else:
            print("Error: Invalid choice. Please enter D, W, V, or E.")
    print("ATM program has ended.")

main()