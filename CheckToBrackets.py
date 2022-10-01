## Q8. Write a program to check if all the brackets are closed in a given code snippet.
from inspect import stack


str=input("Enter the Brackets :")
stack=[]
for i in range(len(str)):
    if (str[i]=="[" or str[i]=="{" or str[i]=="("):
        stack.append(str[i])
    elif (len(stack)!=0 and stack[-1]=="[" and str[i]=="]"):
        stack.pop()
    elif (len(stack)!=0 and stack[-1]=="{" and str[i]=="}"):
        stack.pop()
    elif (len(stack)!=0 and stack[-1]=="(" and str[i]==")"):
        stack.pop()
    else:
        print(False)
if len(stack)==0:
    print(True)
else:
    print(False)