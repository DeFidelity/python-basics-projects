# programing_dictionaries = {"Bug": "An error in a program that prevents the program from running as expected. ", 
# "Function": "A pieece of code that you caneasily call over and over again.",
# }
# #Retrieving item from a dictionary 
# # print(programing_dictionaries["Bug"])

# # #Adding item to a dictionary
# # programing_dictionaries["loop"] = "The action of doing something over and over again."

# # # for the purpose of later adding its good to create an empty dictionary at the begining of a program for later addings
# # # Creating an empty dictionary
# # ampty_dictionary = {}

# # #it's also possible to wipe an existing dictionary just by doing very useful when trying to wipe a dictionary completely maybe a user informatio or maybe a user wants to restart a game.

# # programing_dictionaries = {}
# # print(programing_dictionaries)

# #editing an item in a dictionary
# programing_dictionaries["Bug"] = "A moth in your computer."
# print(programing_dictionaries["Bug"])
# #looping through a dictionary
# for key in programing_dictionaries:
#     print(key)
#     print(programing_dictionaries[key])

    # challenge

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# #Criteria
# # Scores 91 - 100: Grade = "Outstanding"

# # Scores 81 - 90: Grade = "Exceeds Expectations"

# # Scores 71 - 80: Grade = "Acceptable"

# # Scores 70 or lower: Grade = "Fail"

# #TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}

# #TODO-2: Write your code below to add the grades to student_grades.👇
# for key in student_scores:
#     score = student_scores[key]
#     if score >= 91:
#         student_grades[key] =  "Outstanding"
#     elif score >= 81:
#         student_grades[key] = "exceed espectation"
#     elif score >= 71:
#         student_grades[key] = "Acceptable"
#     elif score <= 70:
#         student_grades[key] = "Fail"
#     # for key in student_scores range(91, 100):
#     #     student_grades[key] = "outstanding"
    

# # 🚨 Don't change the code below 👇
# print(student_grades)

# ##############################  Nesting  ######################

# capitals = {
#     "france": "paris",
#     "germany": "Berlin"
# }
# #nesting a list in a dictionary
# travelLog = {
#     "France": {"citiesVisited": ["Lille", "paris", "Dilon"], "total_visits": 12},
    
#     "Nigerai": {"StatesVisited": ["Oyo", "Lagos", "CrossRiver"], "citiesVisited": ["saki", "Ibadan", "calabar"]},
# }

# #nesting dictionary in a list
# travelLog = [
# {
#     "country": "France", 
#     "citiesVisited": ["Lille", "paris", "Dilon"],
#     "total_visits": 12
# },
# {
#     "country": "Nigerai", 
#     "StatesVisited": ["Oyo", "Lagos", "CrossRiver"], 
#     "citiesVisited": ["saki", "Ibadan", "calabar"],
#     "NumberOfVisits": 45
# },
# ]

# Challenge

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country, num_time, citylist):
#     new_country ={}
#     new_country["country"] = country
#     new_country["visits"] = num_time
#     new_country["cities"] = citylist
#     travel_log.append(new_country)



# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

  # Blind Auction
from art import logo 
print(logo)
return = True
while returnit:
    name = input("please input your name \n")
    price = input("please input your bid price \n $")
    theDIc = []

    def method(nameinput, priceinput):
        bidders = {}
        bidders["name"] = nameinput
        bidders["price"] = priceinput
        theDic.append(bidders)
    otherbidders = input("are there any other bidders? \n")
    if otherbidders == "no":
        returnit = False
    else print
method(nameinput=name, priceinput=price)
print(method)

