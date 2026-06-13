# index of the largest element in the list
my_list = [5,4,17,15,25,2006]
curent=my_list[0]
for i in my_list:
    largest=i>curent
print(i)
''''''
# count how many times the largest element appears
my_list=(2,4,5,67,25,67,67)
curent=my_list[0]
for i in my_list:
    largest=i>curent
print(my_list.count(i))
''''''
# check if the list is sorted in ascendig order
my_list = [1,2,3,4,5,6]
if my_list == sorted(my_list):
    print("sorted")
else:
    print("not sorted")
''''''
# check if the key exits in the list
my_list=(1,2,3,4,5,6)
key=8
for i in my_list:
    if i==key:
        print("key exists")
        break
else:
     print("key does not exist")   
''''''
# find the difference between sum of even numbers and sum of odd numbers
my_list=[1,2,3,4,5,6,7,8]
even_sum=0
odd_sum=0
for i in my_list:
  if i%2==0:
    even_sum=even_sum+i
  else:
    odd_sum=odd_sum+i
difference=even_sum-odd_sum
print(difference)
''''''
# remove all occurrences of a given number and print the updated list
my_list=[1,2,3,4,4,5,3,5]
key=5
numbers=[]
for i in my_list:
    if i!=key:
        numbers.append(i)
print(numbers)        
''''''
# create a new list where each elament is doubled and print the new list
numbers = [1, 2, 3, 4]
new_list = []
for i in numbers:
    new_list.append(i * 2)
print(new_list)

     
     


  
   
        


    


