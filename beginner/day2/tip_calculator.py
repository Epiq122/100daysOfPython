# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60


print("Welcome to the tip calculor")
bill = float(input("How much was the bill total? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_percentage = tip / 100
people = int(input("How many people were at the table? "))
total = bill / people
total_bill = float((bill * tip_percentage) / people).round()
print(
    f"The total bill is ${total} split between {people} people and the tip per person is ${total_bill}"
)
