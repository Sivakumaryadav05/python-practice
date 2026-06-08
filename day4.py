# This program prints the numbers from 1 to 1000
for n in range(1,1001):
    print(n)
''''''
# multiplication table
n=int(input("enter the number to print table:"))
for i in range(1,11):
    print(n,'*',i, '=' ,n*i)
''''''''''''
# print all even numbers from 1 to n
n=int(input("enter the number:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)
''''''''''''''
# print all odd numbers from 1 to n
n=int(input("enter the number"))
for i in range(1,n+1):
    if i%2!=0:
        print(i)
'''''' 
# factorial of a number
n=int(input("enter the number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of", n ,"is",fact)       



