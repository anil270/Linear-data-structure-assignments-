## Q10. Write a program to find the smallest number using a stack.
stack=[]
number=int(input("size of stack :"))
for i in range(number):
    ele = int(input("Enter the elements of the stack :"))
    stack.append(ele)
print("Stack elements   :",stack)
minimum=stack[i]
while stack:
    val=stack.pop()
    minimum=min(val, minimum)
print("Smallest elememnts of stack :",minimum)