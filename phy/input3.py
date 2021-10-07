#loops
cars = ["lamborgini", "Ferari", "bugatti", "maserati"]
#to loop trough this lists we have to asssign another verriable as this
#using the "for" function
# for car in cars:
#     print(car)
# #incase a need arise for adding a suffix to each of the loop item
#     print(car + " Fideht")
# #Average Hight calculator
# print(" welcome to the student height calculators")
# studentHeight = input("input a lists of student heights \n").split()
# for n in range(0, len(studentHeight)):
#     studentHeight[n] = int(studentHeight[n])
# # print(studentHeight)
# heightAdd = 0
# for height in studentHeight:
#     heightAdd += 1
# heightlen = 0
# for height in studentHeight:
#      heightlen += 1
# averageHeght = round(heightAdd / heightlen)
# print(averageHeight)

#max score printer
# studentScore = input("Input a list of student scores separated by a space and coma ")
# for n in range(0, len(studentScore)):
#     studentScore[n] = int(studentScore[n])
#     print(studentScore)

# highest = 0
# for score in studentScore:
#     if  score > highest:
#         highest = score
# print(f"THe highest score in the class is: {highest}")

#for loop and the range function
# add = 0
# for number in range(1, 101):
#     add += number
# print(add)

# #adding evens
# even = 0
# for number in range(2, 101,2):
#     even += number
# print(even)

# #FIzbuzz
# for fiz in range(1, 101):
#     if (fiz % 3 == 0) and (fiz % 5 == 0):
#         print("fizzBuzz")
#     elif fiz % 3 == 0:
#         print("fizz")
#     elif fiz % 5 == 0:
#         print("buzz")
    
#     else:
#         print(fiz)

# Reeborg move
# def turnAround():
#     turn_left()
#     turn_left()
#     turn_left()
# def aStep():
#     move()
#     turn_left()
#     move()
#     turnAround()
#     move()
#     turnAround()
#     move()
# aStep()
# turn_left()
# aStep()
# turn_left()
# move()
# turn_left()
# turnAround()
# turn_left()
# move()
# turnAround()
# move()
# turnAround()
# move()
# turn_left()
# aStep()
# turn_left()
# aStep()
# turn_left()
# aStep()
# #but canbe shirten as
# def turnRight():
#     turn_Left()
#     turn_left()
#     turn_left()
# def jump():
#     move()
#     turn_left()
#     move()
#     turnRight()
#     move()
#     turnRight()
#     move()
#     turn_left()
#     for steps in range(6):
#         jump()
