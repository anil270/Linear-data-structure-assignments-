## Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
from array import array


array=[]
number=int(input("size of array :"))
for i in range(number):
    ele = int(input("Enter the elements of the array :"))
    array.append(ele)
print("Original Array :",array)
i = 0
j=number-1
while i<j:
    temp=array[i]
    array[i]=array[j]
    array[j]=temp
    j = j - 1
    i = i + 1
print("Reverse Array :")
for i in range(number):
    print(array[i])