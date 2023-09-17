"""
DAY 2 - TIP CALCULATOR
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
"""
print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? £"))
tip_percent = float(input(
    "What percentage tip would you like to give? 10, 12 or 15? ")
)
party_size = int(input("How many people to split the bill? "))

final_bill = (bill / 100 * tip_percent) + bill

split_bill = round(final_bill / party_size, 2)

print(f"Each person should pay: £{split_bill}")
