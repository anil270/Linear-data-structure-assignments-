## Q9. Write a program to reverse a stack.
stack=[]
number=int(input("size of stack :"))
for i in range(number):
    ele = int(input("Enter the elements of the stack :"))
    stack.append(ele)
print("Normal Stack is :",stack)
temp=[]
while stack:
    temp.append(stack.pop())
for i in temp:
    stack.append(i)
print(stack)



    