# 1) Write a Python program to print even numbers from 1 to 100.
n = 100
print("list of even number in 1 to 100")
for i in range(1, n+1):
    if i % 2 == 0:
        print(i,end=",")


# 2) Write a Python program to print odd numbers from 1 to 100.
n = 100
print("list of odd number in 1 to 100")
for i in range(1, n+1):
    if i % 2 != 0:
        print(i,end=",")


# 3) Write a Python program to find square root of a number.
import math
n = float(input("Enter the number:"))
print("squre root:", math.sqrt(n))


# 4) Write a Python program to find sum of first 20 even numbers.
sum = 0
c = 1
for i in range(1, 100):
    if c <= 20:
        if (i % 2 == 0):
            sum += i
            c += 1
print(sum)


# 5) Write a Python program to count number of digits in entered number.
n = int(input("Enter the number:"))
temp = n
c = -1
while temp != 0:
    temp = int(temp)/10
    c += 1
print("count of given number is:", c)


# 6) Write a Python program to find factors of a given number.
n = int(input("Enter the number:"))
print("The factor of ", n, " are:")
for i in range(1, n+1):
    if n % i == 0:
        print(i)


# 7) Write a Python program to check whether the entered number is palindrome or not.
n = int(input("Enter the number:"))
temp=n
r=0
while temp!=0:
    a=temp%10
    r=r*10+a
    temp=temp//10
if n==r:
    print(n," is pelindrom number")
else:
    print(n," is not pelindrom number")
    

# 8) Write a Python program to concatenate two strings.
s1=str(input("Enter first string:"))
s2=str(input("Enter second string:"))
s1=s1+" "+s2
print(s1)


# 9) Write a Python program to convert string into uppercase.
s1=str(input("Enter string:"))
s2= s1.upper()
print(s2)


# 10) Write a Python program to count Vowels in a given string.
n=str(input("Enter string:"))
c=0
for i in n:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c+=1
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        c+=1
print("count of vowels:",c)        


# 11) Write a Python program to reverse a given string.
#reverse by character
n=str(input("Enter string:"))
s1=reversed(n)
print("".join(s1))

#==========OR=========#
#reverse by words
n=str(input("Enter string:"))
s1=n.split()
s1=list(reversed(s1))
print("".join(s1))