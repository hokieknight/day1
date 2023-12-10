# comment
name = "Blah" #input("What is your name? ")
print("Hello " + name)
length = len(name)
print(length)
print("hello world\nbye world")
print("hello"[4])

somenum = 123_456_789
print(somenum)
print(type(somenum))
print(type(str(somenum)))

print(f"some number = {somenum}")
print(8//3)  #trunc to int
print(2**3) #exponent

num = 101   
if num % 2 == 0:
    print (f"{num} is even")
else:
    print(f"{num} is odd")

age = 17
if age < 12:
    print("Pay $5")
elif age < 18:
    print("Pay $7")
else:
    print("Pay $12")


year = 2024
isLeapYear = False
if year % 4 == 0:
    isLeapYear = True
if year % 100 == 0:
    isLeapYear = False
if year % 400 == 0:
    isLeapYear = True
if isLeapYear:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

import random

rint = random.randint(1,100)
print(f"random # {rint}")

import my_mod
print(my_mod.pi)
