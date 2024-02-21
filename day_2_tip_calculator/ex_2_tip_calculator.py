print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage of tip you like to give? "))
people_num = int(input("How many people to split the bill? "))
cost_per_person = total_bill * (1 + tip_percentage / 100) / people_num
print(f"Cost per person is equal to {round(cost_per_person, 2)}$")