# number is positive
n=int(input("enter the number"))
if n>0:
    print("number is positive")
else:
    print("number is negative")    
''''''
#number is divisible by 5
n=int(input("enter the number"))
if n%5==0:
    print("the given number is divisible by 5")
else:
    print("Not divisible by 5")    
''''''
# a person is eligible to vote or not
age=int(input("enter your age"))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")    
''''''
# the number is even or odd
n=int(input("enter the number"))
if n%2==0:
    print("number is even")
else:
    print("number is odd")  
''''''
# largest of two numbers
n1=int(input("enter the first number"))  
n2=int(input("enter the second number"))
if n1>n2:
    print("first number is greater")
else:
    print("second number is greater")    
''''''
# student pass or fail
marks=int(input("enter the marks"))
if marks>=35:
    print("pass")
else:
    print("fail")    
''''''
# number is positive or negative or zero
n=int(input("enter the number"))
if n>0:
    print("the given number is positive")
elif n<0:
    print("the given number is negative")
else:
    print("the number is zero")       
''''''
# person is child or teenager,adult,or senior
age=int(input("enter your age"))
if age<12:
    print("child")
elif age<18:
    print("adult")
elif age<40:
    print("teenager")
else:
    print("senior citizen")      
''''''''
# largest among three numbers
n1=int(input("enter the first number"))
n2=int(input("enter the second nmber"))
n3=int(input("enter the third number"))
if n1>n2 and n1>n3:
    print("1st no is greater")
elif n2>n1 and n2>n3:
    print("2nd no is greater")   
else:
    print("3rd no is greater")      
''''''''
# conditional statement problem
purchased_amount=float(input("enter the purchased amount in a shopping")) 
if purchased_amount>5000:
    print("you won 20 percente discount")
    final_price=purchased_amount*80/100
    print(final_price)
else:
    print("thank you")       
    
