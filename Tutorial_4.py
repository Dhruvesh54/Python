# 1. Write a Python program to Calculate the sum of the series 1 +11 + 111 + 1111 + .. n terms.
sum = 0
t = 1
n = int(input("Enter the number:"))
for i in range(1,n+1):
    print (t,end="")
    if(i<n):
        print("+",end="")
    sum +=t
    t=(t*10)+1
print()
print(sum)


# 2. Write a Python program to check whether a given number has a pure cube root or not.
n=int(input("Enter the number:"))
print(n**(1/3))

#pure cube root or not
n=int(input("Enter the number:"))
n=abs(n)
ans=round(n**(1/3))**3==n
print(ans)


# 3. Write a Python program to get sum of Fibonacci series till number entered by user.
n=int(input("Enter the number:"))
a=0
b=1
s=a+b
print(a,end=" ")
print(b,end=" ")
for i in range(2,n):
    temp=a+b
    s+=temp
    print(temp,end=" ")
    a=b
    b=temp
print("\nsum of fibonaci series :",s)


# 4. Write a Python program to check whether a number is a Strong Number or not.
n=int(input("Enter the number:"))
sum=0
temp=n
while(temp!=0):
    r=temp%10
    fact=1
    for i in range(1,r+1):
        fact*=i
    sum+=fact    
    temp=int(temp/10)   
if sum==n:
    print("strong number")
else:
    print("not strong number")


# 5. Write programs in Python to display below patterns with dynamic values,
# *            1         1                        *
# * *          2 3       4 9                    *   *
# * * *        4 5 6     16 25 36             *   *   *
# * * * *      7 8 9 10  49 64 81 100       *   *   *   *
# * * * * *                                   *   *   *
#                                               *   *
#                                                 *

# 1
a=int(input("Enter the number:"))
for i in range (1,a):
    for j in range (i):
        print(end="*")
    print()


# 2
a=int(input("Enter the number :"))
num = 1
for i in range (1,a+1):
    for j in range (1,i+1):
        print (num,end=" ")
        num=num+1
    print()


# 3
a=int(input("Enter the number :"))
num = 1
for i in range (1,a+1):
    for j in range (1,i+1):
        print (num**2,end=" ")
        num=num+1
    print()


# 4
n = int(input("Enter the number:"))
k = 2 * n - 2
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print(" ")
k = n - 2
for i in range(n, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print(" ")