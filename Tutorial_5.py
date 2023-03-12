# 1) Write a Python program to find LCM and GCD of given numbers using user defined function.

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))

def lcm_gcd(a,b):
    temp=a
    temp1=b
    while temp1!=0:
        t=temp1
        temp1=temp%temp1
        temp=t
    gcd=temp
    lcm=(a*b)/gcd
    print("LCM : ",lcm)
    print("GCD : ",gcd)
lcm_gcd(a,b)


# 2) Write a Python program to find prime number using user defined function.

num1=int(input("Enter number :"))
def prime(num1):
    flag = 0
    for i in range(2,num1+1):
        if num1 % i==0:
            flag+=1
    if flag == 1:
        print("Number is Prime")
    else:
        print("Number is Not prime")

prime(num1)     


# 3) Write a Python program to print Fibonacci series using user defined function.

a = int(input("Enter the number:"))
b = a-1
def fab(b):
    n1 = 0
    n2 = 1
    c = 1
    print("series is:",n1)
    print(n2)
    while c != b:
        s = n1+n2
        t = s
        n1 = n2
        n2 = t
        c += 1
        print(s)
fab(b)


# 4) Write a Python program to find factorial of a given number using user defined function.

n=int(input("Enter the number:"))
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)    
fact(n)


# 5) Write a Python program to check whether the entered number is Armstrong number or not using user defined function.

n=int(input("Enter the number:"))
def arm(n):
    temp=n
    ans=0
    while temp!=0:
        a=int(temp%10)
        ans+=a*a*a
        temp/=10
    if n==ans:
        print("Number is armstrong")
    else:
        print("Number is not armstrong")
arm(n)

# 6) Write a Python program to explain concept of arbitrary argument using three or more functions.

def f1(*l1):
    print(l1)
f1(1,2,3,4)

def f2(*l1):
    print(l1[1])
f2(5,6,7,8)

def f3(*l1):
    r=0
    for i in l1:
        r+=i
    print("sum",r)   
f3(9,10)

# 7) Write a Python program to explain default argument using defined function

def f4(a=1,b=2):
    sum=a+b
    print(sum)
f4(3,2)
