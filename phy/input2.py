# # import random

# # randomInteger = random.randint(1, 10)
# # print(randomInteger)

# # #rand float is from 0.0000 - 0.9999
# # randomFloat = random.random(),5
# # print(randomFloat)

# # #if we have to give it a limit we would have to multiply randomFloat by the limit.

# # #code challenge
# # testSeed = int(input("create a seed below"))
# # random.seed(testSeed)

# # randSide = random.randint(0,1)

# # if randSide == 1:
# #     print("Heads")
# # else:
# #     print("Tails")

# #creating a lists in python.
# #lists = ["item 1" "item 2" "item 3"]

# #Banker Roullet who will pay the bill
# import random
# testSeed = int(input("create a seed Number"))
# random.seed(testSeed)

# #spliting string into lists
# namesAsCVS = input("provide names: and separate by comma. ")
# names = namesAsCVS.split(", ")
# #generating a random name for the payment
# numbers = int(len(names)) #get num of item in lists
# randName = random.randint(0,numbers -1) #generate random number between them
# gen = names[randName] #caling the name coresspond to the num generated
# print(f"{gen} is paying the money today ")

# #the code can be simplify just by using th e choice variable
# personToPay = random.choice(names)
# print(personToPay + "is going to buy the meal")




