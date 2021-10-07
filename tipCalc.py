print("Welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("How much would you like to give? 10, 20, 30?"))
people = int(input("How many people to split the Bill?"))
tipAsPercent = tip / 100
totalTipAmount = bill * tipAsPercent
totalBill = bill + totalTipAmount
billPerPerson = totalBill / people
finalAmount = round(billPerPerson, 2)
print(f"Each person should pay {finalAmount}")
