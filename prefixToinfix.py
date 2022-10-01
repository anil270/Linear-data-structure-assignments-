## Q7. Write a program to convert prefix expression to infix expression
from inspect import stack


str1 = input("Enter the String :")
stack=[]
c=len(str1)-1
while c>=0:
    if str1[c] == "*" or str1[c] == "+" or str1[c] == "-" or  str1[c] == "/" or str1[c] == "^" or str1[c] == "(" or str1[c] == ")":
        a=stack.pop()
        b=stack.pop()
        s1=""
        s1=a+str1[c]+b
        stack.append(s1)
        b=' '.join(map(str, stack))
    else:
        stack.append(str1[c])
    c=c-1
print("("+b+")")
