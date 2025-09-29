class MoneyNotEnoughError(Exception):
    """Insufficient funds for the requested transaction"""
    pass
class PINCodeError(Exception):
    """Invalid PIN code"""
    pass
class UnderageTransactionError(Exception):
    """You must be 18 years or older to perform online transactions"""
    pass
class MoneyIsNegativeError(Exception):
    """The amount of money cannot be a negative number"""
    pass

pin, balance, age = [int(x) for x in input().split(", ")]
MIN_AGE = 18

while (command:=input()) != "End":
    command = command.split("#")
    if command[0] == "Send Money":
        money = int(command[1])
        pin_code = int(command[2])

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if pin != pin_code:
            raise PINCodeError("Invalid PIN code")

        if age < MIN_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif command[0] == "Receive Money":
        money = int(command[1])
        if money<0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        remaining_money=0.5*money
        balance += remaining_money
        print(f"{remaining_money:.2f} money went straight into the bank account")