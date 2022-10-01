## Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.
str1 = input("Enter the String :")
str2=str1[::-1]
stack=[]
c=len(str2)-1
while c>=0:
    if str2[c] == "*" or str2[c] == "+" or str2[c] == "-" or  str2[c] == "/" or str1[c] == "^" or str1[c] == "(" or str1[c] == ")":
        a=stack.pop()
        b=stack.pop()
        s1=""
        s1=a+b+str2[c]
        stack.append(s1)
        b=' '.join(map(str, stack))
        d=b[::-1]
    else:
        stack.append(str2[c])
    c=c-1
print("Before expressions :",str1)
print("After expressions :",d)