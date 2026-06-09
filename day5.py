# sum of first n natural numbers 
n=int(input("enter the number:"))
sum=0   
for i in range(1,n+1):
    sum=sum+i
print("sum of first", n ,"natural numbers is:",sum)
''''''
# multiplication table
n=int(input("enter the number to print table:"))
for i in range(1,11):
    print(n,'*',i, '=' ,n*i)
''''''''''''
# count digits in a number
n=int(input("enter the numbers:"))
count=0
while n>0:
    n=n//10
    count=count+1
print("count of numbers is:",count)
''''''''
# reverse a given number
n=int(input("enter a number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)   
''''''
# prime number
n=int(input("enter a number:"))
is_prime=True
for i in range(2,n):
    if n%i==0:
        is_prime=False
if is_prime:
    print(n,"is prime")
else:
    print(n,"is not a prime")            
