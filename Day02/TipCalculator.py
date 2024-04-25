print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
tip_percentage = percentage / 100 + 1
splited_amt = round((bill * tip_percentage) / num_of_people, 2)
print(f"each persion should pay: ${splited_amt}")