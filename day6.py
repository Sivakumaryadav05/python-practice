# basic array program
array=[15,17,5,25,4]
for i in array:
    print(i)
''''''
# sum of all elements
array=[15,17,5,25,4]
sum=0
for i in array:
    sum=sum+i
print("sum of all elements is:",sum)  
''''''
# largest element in an array
arr = [3, 7, 1, 9, 4]
largest = arr[0]
for x in arr:
    if x > largest:
        largest = x
print("Largest =", largest)
''''''
# smallest element in an array
arr=[5,25,17,15,11,7]
smallest=arr[0]
for x in arr:
    if x < smallest:
        smallest=x
print("smallest number is:",smallest)    
''''''
# count even numbers
arr=[5,15,6,8,9,2]
count=0
for x in arr:
    if x%2==0:
     count=count+1
print(count)     
''''''
# print only odd numbers
arr=[17,15,11,56]
count=0
for x in arr:
    if x%2!=0:
        count=count+x
        print(count)
''''''
# count elements greater than 10
arr=[1,23,45,67,8,78]
count=0
for x in arr:
    if x>10:
        count=count+1
print(count)
''''''
# square of each element
arr=[2,4,5,7,8]
square=[]
for x in arr:
    square.append(x*x)
print(square)
''''''
# print elements in a reverse order
arr = [3, 7, 1, 9, 4]
for i in range(len(arr)-1, -1, -1):
  print(arr[i])
''''''
# average of all elements
arr=[2,4,5,78,54,34]
total=0
for x in arr:
    total=total+x
    avg=total/len(arr)
print(avg)    



