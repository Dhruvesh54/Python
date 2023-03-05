# 1) Write a Python program to find maximum from given two numbers.

a = int(input("Enter number:"))
b = int(input("Enter number:"))

if a>b:
    print (a,"is maximum")
else:
    print (b,"is maximum")


# 2) Write a Python program to find maximum from given three numbers.

a = int(input("Enter number:"))
b = int(input("Enter number:"))
c = int(input("Enter number:"))

if a>b:
    if a>c:
        print (a,"is maximum")
    else:
        print (c,"is maximum")
else:
    if b>c:
        print (b,"is maximum")
    else:
        print (c,"is maximum")


# 3) Write a Python program to print natural numbers.

n = int(input("Enter number:"))
if n<0:
    print ("Please Enter positive number")
else:
    for i in range (1,n):
        print(i)


# 4) Write a Python program to check whether a year is leap year or not.

y = int(input("Enter year:"))
if y%4==0 and y%100!=0 or y%400==0:
    print (y,"is leap year")
else:
    print(y,"is not leap year")


# 5) Write a Python program to find odd or even number.

n = int(input("Enter number:"))
if n%2==0:
    print (n,"is even")
else:
    print (n,"is odd")


# 6) Write a Python program to check whether a number is negative or not.

n = int(input("Enter number:"))
if n<0:
    print (n,"is negative number")
elif n==0:
    print (n,"is Zerro")
else:
    print (n,"is not negative number")