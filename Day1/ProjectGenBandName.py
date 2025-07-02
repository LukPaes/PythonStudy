# This code generates a band name based on the user's input for their city and pet name.
# It prompts the user for their city and pet name, then combines them to create a band name.
# The final band name is printed to the console.
print("Welcome to the Band Name Generator!")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's the name of a pet?\n")
band_name = city + " " + pet
print("Your band name could be: " + band_name)


