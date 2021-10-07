#to comment out its control slash(/)
#multiple next line shortcut
# print("Hello world\nHelloworld!")
# #python concaTENation
# print("Hello" + " " + "Angella")

#debugging FIX THE CODE

# print("Day 1 - String Manipulation")
# print('String concatenation is done with the "+" sign')
# print('e.g. print("hello" + "world")')
# print("New lines can be created with a backslash and n. ")

#The Input
# firstname = input("ENter your first name : ")
# Lastname = input("Enter your last name : ")

# print("Your Full Name is ", firstname,Lastname)

# #using the concatenation to merge two functoons
# print("Hello " + input('Your name: '))

#print( len( input (" TYPE ANYTHING YOU WANTS TO CALCULATE") ) )

#PYTHON VARIABLES
# name = input("what is your name ")
# print(name)

# veriable exercise
# a = input("a: ")
# b = input("b: ")
# c = a
# a = b
# b = c
# print("a = " + b)
# print("b = " + b)

#Data types
#string
# print("adeyemihaki"[4])
# print("123" + "345") 
#Integer all whole numbers are called integer in python.
# print(123+34)
#all decimal places are called Float

#Boolean (the value of true or false)
# the 'type' function help know what type of element we area having.
#Code excersice
# two_digit_num = input("Type a two digit number")
# A = (two_digit_num[0])
# B = (two_digit_num[1])
# result = int(A) + int(B)
# print(result)

#code challenge Calulating weight BMI
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# BMI = int(weight) / float(height)**2 
# BMI_int = int(BMI) #to get it without Decimal
# print(BMI_int)

#number manipulation
#rounding a decimal use the 'round' function
#print(round(8/3, 2)) #the digit after coma i]determine the number of digit you want to place after decimal.
#when doing a subtraction  operation we can use // instead of one to round things off without decimal.
# f string cna be use to collate diffrent data types together instead of changing the data type
# score = 0
# height = 1.8
# isWinning = True
# #using fstring
# print(f"your score is{score}, your height is {height}, youre winning is {isWinning}")

#code challenge

# age = input("What is your current age?")
# days = 365
# weeks = 52
# months = 12
# x = (90 - int(age)) * 365
# y = (90 - int(age)) * 52
# z = (90 - int(age)) * 12
# message = f"You have {x}days, {y}weeks and {z}months left."
# print(message)

# if and else statement

#building a ticket requirement replacer that would certify if our guest can have access or not
print("Welcome to the Rollercoaster")
height = int(input("what is your height in cm? "))
bill = 0
if(height >= 120):
 print("Congratulations, you can proceed to the Rollercoaster")
 age = int(input("what is your age? "))

 if age >= 18 and age < 45 :
   bill = 12
   print("Adult tickets are $12 ")
 if age > 45 and age < 55:
   bill = 0
   print("Everything is gonna be okay, you got a free ride on us ")   
     

 elif age <= 12:
   bill = 5
   print("child tickets are $5")
     
  

 else:
   bill = 7
   print("youth tickets are $7")
     
  
 wantsPhoto = input("Do you want a photo taken? Y or N.")
 if wantsPhoto == "Y":
    bill += 3
    print(f"Your final bill is {bill}")
else:
  print("sorry, you have to grow taller before you can ride")
   

#coding exercise Building an even and odd number tracker

# number = int(input("which number do you want to check"))
# remainder = number % 2
# if(remainder == 0):
#     print("Its even")
# else:
#     print("Its Odd")

#BMI(Body Mass Index) 2.0 weight ND HEIGHT CHECKER UPGRADE

# height = float(input("enter your weight in m:"))
# weight = float(input("enter your weight in kg: "))
# result = round(weight / height ** 2)
# if result < 18.5:
#     print(f"BMI {result} shows that you are under weight!!!") 
# elif result < 25:
#     print(f"BMI {result} shows that you have normal weight!!!")
# elif result < 30:
#     print(f"BMI {result} shows that you are overweight!!!")
# elif result < 35 :
#     print(f"BMI {result} shows that you are Obese!!!")
# else:
#     print(f"BMI {result} shows that you are clinically obese!!!")
 
#challenge 2 checking if a year is leap or not

#year that can be divided by 4 is leap 
#unless if it can be divided by 100
#and unless it can be divided by 400

# year = int(input("Which year do you want to check? "))
# leapCheck2 = year % 4 
# if leapCheck2 == 0:
#     leapcheck1 = year % 100
#     if leapcheck1 == 0:
#         finalCheck = year % 400
#         if finalCheck == 0:
#             print("WOW thats a leap year")
# else:
#     print("Its not a leap year!")

# pizza order program
# print("Welcome to python pizza deliveries! , ")
# size = input("What size of pizza do you want? S, M or L ")
# addPeperoni = input("Do you want peperoni? Y or N ")
# extraCheese = input("Do you want extra cheese? Y or N")
# Scost = 15
# Mcost = 20
# Lcost = 25
# if size == "S":
#   print(f"small pizza costs ${Scost}")
#   if addPeperoni == "Y":
#     Scost += 2
#     print(F"Small pizza and peperoni costs ${Scost} ")
#   else:
#     print(f"your Final bill is {Scost}")
#   if extraCheese == "Y":
#       Scost += 1
#       print(f"Your Final bill is ${Scost}")
#   else:
#       print(f"your Final bill is {Scost}")
# elif size == "M":
#   print(f"Medium pizza costs ${Mcost} ")
#   if addPeperoni == "Y":
#     Mcost += 3
#     print(F"Small pizza and peperoni costs ${Mcost} ")
#   else:
#     print(f"your Final bill is {Mcost}")
#   if extraCheese == "Y":
#       Mcost += 1
#       print(f"Your Final bill is ${Mcost}")
#   else:
#       print(f"your Final bill is {Mcost}")
# elif size == "L":
#   print(f"Large size pizza costs ${Lcost}")
#   if addPeperoni == "Y":
#     Lcost += 3
#     print(F"Small pizza and peperoni costs ${Lcost} ")
#   else:
#     print(f"your Final bill is {Lcost}")
#   if extraCheese == "Y":
#       Scost += 1
#       print(f"Your Final bill is ${Lcost}")
#   else:
#       print(f"your Final bill is {Lcost}")

# i didnt get it too right, it should be simply

print("Welcome to python pizza delieveries")
size = input("What size of pizza do you want? S, M or L ")
peperoni = input("do you want extra peperoni? Y or N")
cheese = input("do you want extra cheese? Y or N")
bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25

if peperoni == "y":
  if size == "S":
    bill += 2
  else:
    bill += 3
if cheese == "Y":
  bill += 1
print(f"Your final bill is ${bill}")

#Building a Love calculator

print("welcome to the Love Calculator!")
name = input("What is your name? \n ")
name2 = input(" what is your crush name? \n ")
combinedName = name + name2
LName = combinedName.lower()

t = LName.count("t")
r = LName.count("r")
u = LName.count("u")
e = LName.count("e")
true = t + r + u + e

l = LName.count("l")
o = LName.count("o")
v = LName.count("v")
e = LName.count("e")
love = l + o + v + e

loveScore = int(str(true) + str(love))
if (loveScore < 10) or  (loveScore > 90):
  print(f"Your love score is {loveScore} you go together like coke and mentos ")
elif (loveScore >= 40) and (loveScore <= 50):
  print(f"Your love score is {loveScore}, you area alright together")
else:
  print(f"your score is {loveScore} you are alrigt together")




