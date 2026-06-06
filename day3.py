# number is divisible by 3 and 5
n=int(input("enter the number"))
if n%3==0 and n%5==0:
    print("number is divisible by 3 and 5")
else:
    print("the number is not divisible by 3 and 5")    
''''''''
# Atm problem
withdraw_amount=float(input("enter the withdrawal amount"))
balance=50000
if withdraw_amount<balance:
    cash=balance-withdraw_amount
    print("available balance:",cash)
else:
    print("insufficient balance")   
''''''''
# student eligiblity check
marks=int(input("enter your marks:"))
cer=str(input("you have any sports certificate?"))
if marks>=75 and cer=="yes":
    print("you are eligible for the admission")
else:
    print("you are not eligible for the admission")
''''''''
# wheather year is a leap year or not
year=int(input("enter the year"))
if year%4==0 and year%100!=0 or year%400==0:
    print("the given year is a leap year")