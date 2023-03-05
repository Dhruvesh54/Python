#1)Write a Python program to print “Welcome”.
print("Welcome")


#2)Write a Python program to print any message using different variations of print ()method.

print("hello world")
print("hello","world")
print("hello",end=" world")


#3) Write a Python program to declare different types of variables, print their values and types.

num = 12
string = "Hello"
fl = 12.3
print(type(num))
print(type(string))
print(type(fl))


#4)Write a Python program to add, subtract, multiply and divide any two numbers.

num1 = 12
num2 = 12
print("Addition",num1+num2)
print("Substraction",num1-num2)
print("multiplication",num1*num2)
print("division",num1/num2)


#5) Write a Python program to explain all arithmetic operator with example.

opr1 = 2
opr2 = 3

print(opr1+opr2)

print(opr1-opr2)

print(opr1*opr2)

print(opr1/opr2)

print(opr1%opr2)

print(opr1**opr2)

print(opr1//opr2)


#6)Write a Python program to find maximum number from two numbers.

num1 = 5
num2 = 2
if num1>num2:
    print("maximum number is ",num1)
else:
    print("maximum number is ",num2)


#7) Write a Python program to typecast input value to Integer and Float.

a = input("Enter a value")
num = int(a)
fl = float(a)
print(type(num))
print(type(fl))


#8) Write a Python program print multiline string and its length.

string ="""
    MULTILINE STRING
    Dhruvesh kanji bhai vora
"""

print(string)
print("length of string : ",len(string))


#9) Write a Python program to find compound interest.

principal_amount= 1200
time= 2
rate= 5.4
a=principal_amount*(1+(rate/100))**time
ci=a-principal_amount
print(ci)
