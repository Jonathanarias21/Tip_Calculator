
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
bill_as_int = float(bill)
number_of_people = input("How many people are splitting the bill?")
people_as_int = int(number_of_people)
tip = input("What percentage tip would you like to gice? 10, 12, or 15?")
tip_as_int = int(tip)
tip_as_percentage = tip_as_int / 100
total_bill = round(bill_as_int * (1 + tip_as_percentage) / (people_as_int), 2)
final_amount = "{:.2f}".format(total_bill)
pay_per_person = print(f"Each person should pay:  ${total_bill} ")


# This is a test