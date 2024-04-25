age = input("Enter your current age: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
int_age = int(age)
years_left = 90 - int_age
weeks_left = years_left * 52
print(f"You have {weeks_left} weeks left.")