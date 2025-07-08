#Today we going to create a simple bill calculator that will calculate the total amount of the bill including tax and tip.
# The user will input the total bill amount, the tax percentage, and the tip percentage.
print("Welcome to the Bill Calculator!")
bill = float(input("What was the total bill amount? $"))
tax_percentage = float(input("What is the tax percentage? "))
tip_percentage = float(input("What is the tip percentage? "))
# Calculate the total amount of the bill including tax and tip
tax_amount = bill * (tax_percentage / 100)
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tax_amount + tip_amount
# Print the total amount of the bill
print(f"The total amount of the bill is: ${total_bill:.2f}")
# This code calculates the total bill amount including tax and tip based on user input.
# It prompts the user for the total bill amount, tax percentage, and tip percentage,    
# then calculates the tax and tip amounts, and finally prints the total bill amount formatted to two decimal places.
# The use of f-string formatting ensures that the total bill is displayed with two decimal places for better readability.
# The code is simple and straightforward, making it easy to understand and use. 
# The use of float for bill, tax_percentage, and tip_percentage allows for decimal values,
# which is important for accurate financial calculations.
# The code is efficient and does not require any additional libraries or modules, making it lightweight and
# easy to run in any Python environment.
#

