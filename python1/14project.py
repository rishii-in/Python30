class InsufficientBalanceError(Exception):
    pass
class InvalidWithdrawError(Exception):
    pass

try:
    balance=int(input("enter balance:"))
    withdraw=int(input("enter withdraw amount:"))
    if withdraw<=0:
        raise InvalidWithdrawError("Zero or negative Withdrawl")
    if withdraw>balance:
        raise InsufficientBalanceError("Insufficient Balance")

except ValueError:
    print("Invalid Input")
except InsufficientBalanceError as e:
    print(f"Transaction Failed: {e}")
except InvalidWithdrawError as e:
    print(e)
else:
    balance=balance-withdraw
    print("Withdrawal Successful")
    print(f"Balance amount: {balance}")

finally:
    print("ATM session ended")