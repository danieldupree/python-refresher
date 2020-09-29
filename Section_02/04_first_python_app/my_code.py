user_age = input("Enter your age in years: ")
years = int(user_age)
months = years*12
seconds = years*31557600
print(f"Your age, {years}, is equal to {months} months")
print(f"Your age, {years}, is equal to {seconds:,} seconds")
