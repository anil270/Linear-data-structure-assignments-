## Q4. Write a program to print the first non-repeated character from a string?
str1=input("Enter the String :")
for i in str1:
    if (str1.find(i,(str1.find(i)+1))) == -1:
          print("First Non-Repeating Character of String is:",i)
          break
          

