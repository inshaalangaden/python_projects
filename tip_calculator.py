print("Welcome to Tip Calculator!")

total_bill=input("What was the total bill?")

tip=input("How much tip whould you like to give? 10, 12 or 15?")
percentage_tip= float(tip)/100

people_count=input("How many people to split the bill?")

split_bill=round((float(total_bill)+(float(total_bill)*percentage_tip))/float(people_count),2)

print(f"Each person should pay: {split_bill}")