print("Welcome to the tip calculator.")

bill: float = input('What is the total bill ? $ \n')


tip_per: float = input("What percentage tip would you like to give ? 10,12 or 15 ?")


percentage: float = float(tip_per) / 100


number_of_people: int = input("How many people to split the bill ? ")

number_of_people: int = int(number_of_people) 


bill: float = float(bill)


total_bill: float = bill * percentage / number_of_people
print(total_bill)









