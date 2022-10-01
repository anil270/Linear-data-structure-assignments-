## Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
list=[]
number=int(input("size of array :"))
sum=int(input(" Enter the value of sum which you want :"))
count = 0
for i in range(number):
    ele = int(input("Enter the elements of the array :"))
    list.append(ele)
print(list)
n=len(list)
for k in range(n):
    for j in range(k + 1, n):
        if list[k]+list[j]==sum:
            count=count+1
print("Pairs of integer whose sum is equal to a given number :",count)


