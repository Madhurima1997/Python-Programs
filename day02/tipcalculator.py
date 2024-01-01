'''Tip calculator program'''
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
bill = float(input("Enter total bill \n"))
person = int(input("How many people are splitting the bill ? \n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

tipShare = round(((bill/person) * ((100 + tip)/100)),2)
print(f"You need to pay ${tipShare:0.2f}")
