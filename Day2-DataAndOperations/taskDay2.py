print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

billPerPersonMinusTip = bill/people
tipPerPerson = billPerPersonMinusTip * (tip/100)
billPerPersonPlusTip = billPerPersonMinusTip + tipPerPerson

print(f"Each friend should pay a tip of {tipPerPerson} and a total of {billPerPersonPlusTip}")