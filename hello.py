"""Module providing hello world testing."""
import random
import my_mod

NAME = "Blah" #input("What is your name? ")
print("Hello " + NAME)
NAME = "Blah2"
LENGTH = len(NAME)
print(LENGTH)
print("hello world\nbye world")
print("hello"[4])

SOME_NUM = 123_456_789
print(SOME_NUM)
print(type(SOME_NUM))
print(type(str(SOME_NUM)))

print(f"some number = {SOME_NUM}")
print(8//3)  #trunc to int
print(2**3) #exponent

NUM = 101
if NUM % 2 == 0:
    print (f"{NUM} is even")
else:
    print(f"{NUM} is odd")

AGE = 17
if AGE < 12:
    print("Pay $5")
elif AGE < 18:
    print("Pay $7")
else:
    print("Pay $12")


def is_leap_year(year):
    """Function checking leap year."""
    #YEAR = 2024
    is_leap = False
    if year % 4 == 0:
        is_leap = True
    if year % 100 == 0:
        is_leap = False
    if year % 400 == 0:
        is_leap = True
    if is_leap:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
    return is_leap

is_leap_year(2024)
is_leap_year(2000)
print(is_leap_year(2021))

rint = random.randint(1,100)
print(f"random # {rint}")
print(f"random # {random.random()}")

print(my_mod.PI)

states = ["Delaware", "Pennsylvania", "New Jersey"]
states.append("Georgia")
print(states[-2])

for state in states:
    print(state)

for NUM in range(1, 10, 3):
    print(NUM)

print(random.choice(states))
random.shuffle(states)
print(states)

my_mod.myfunc()


if "Delaware" in states:
    print("Yes")

my_dictionary = {
    "Bug": "An Error",
    "Function": "Sub process",
}
my_dictionary["Loop"] = Rrepetitive action"

for key, value in my_dictionary.items():
    print(f"{key}: {value}")
    #print(my_dictionary[key])
