## Q3. Write a program to check if two strings are a rotation of each other?
str1=input("Enter first String :")
str2=input("Enter Second String :")
str3=str1+str1
if str2 in str3:
    print("String are rotation of each other.")
else:
    print("String are not rotation of each other.")
