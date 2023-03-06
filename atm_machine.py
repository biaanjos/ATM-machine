from account import Account


def main():

    accounts = []
    create_initial_accounts(accounts)

    while True:
        input_id = int(input("Enter an account id:"))
        valid_id = check_id(input_id, accounts)
        if valid_id:
            while True:
                operation = menu()
                balance = accounts[input_id].get_balance()
                if operation == 1:
                    print("The balance is ", format(balance, '.2f'))
                    print()
                elif operation == 2:
                    amount = float(input("Enter an amount to withdraw: "))
                    if amount > balance:
                        print("The amount is higher than the current balance! Operation not completed")
                        print()
                    else:
                        accounts[input_id].withdraw(amount)
                        print()
                elif operation == 3:
                    amount = float(input("Enter an amount to deposit: "))
                    accounts[input_id].deposit(amount)
                    print()
                elif operation == 4:
                    print()
                    break
                else:
                    print("Operation invalid!")
                    print()
        elif not valid_id:
            print("Incorrect id!")
            print()


def create_initial_accounts(accounts):
    for i in range(0, 10):
        accounts.append(Account(i, 100.00, 4.5))


def check_id(input_id, accounts):
    valid_key = False
    for key in accounts:
        if key.get_id() == input_id:
            valid_key = True
            break

    return valid_key


def menu():
    print("Main menu")
    print("1: check the balance")
    print("2: withdraw")
    print("3: deposit")
    print("4: exit")
    operation = int(input("Enter a choice:"))

    return operation


main()
