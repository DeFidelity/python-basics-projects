#Normal function 
# def greet():
#     print("Hello")
#     print("how do you do?")
#     print("Isn't the weather nice today?")
# greet()

# #functions that allows for input

# def  greetWithName(name):
#     print(f"Hello {name} ")
#     print(f"how do you do {name} ")
#     print(f"Isn't the weather nice today {name} ")
# greetWithName("Fideh")   

#positional argument

# # function with more than 1 input
def greetWith(name = 1, location = 2):
    print(f"Hello {name}")
    print(f"how is it like in {location}")

#keyword argument

# greetWith ("fideh", "Calabar")
greetWith(location= "calabar", name= "fideh")

#challenge

#area calculator.
import math
def paintCalc(height, width, cover):
    mul = height * width
    total = math.ceil(mul / cover)
    print(f"You'll need {total} cans of paint")

testH = int(input("height of wall: "))
testW = int(input("Width of wall: "))
coverage = 5
paintCalc(height=testH, width=testW, cover=coverage)

#prime Number checker
#Write your code below this line 👇
def prime_checker(number):
is_prime(n)

def is_prime(a):
    x = True 
    for i in (2, a):
            while x:
               if a%i == 0:
                   x = False
               else:
                   x = True


    if x:
        print "prime"
    else:
        print "not prime"





#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#mine

def primeChecker(number)
isPrime = True
for i in range(2, number - 1):
    if number % i == 0:
        isPrime = False
    if isPrime:
        print("it's a prime number")
    else:
        print("its not a prime number. ")
n = int(input("input a number you want to check "))
primeChecker(number= n)



