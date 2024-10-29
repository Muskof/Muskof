print("Welcome to python pizza")
size = input("what  size pizza would you like? S, M, L ")
add_pepperoni = input("would you like pepperoni? Y, N")
add_extra_cheese = input("would you like extra cheese? Y, N")
bill = 0
if size == 'S':
 bill  += 15
elif size == 'M':
 bill += 20
else:
 bill += 25
if add_pepperoni ==  'Y':
 bill  += 2
if add_extra_cheese == 'Y':
 bill  += 1
else:
 # f-string formatting
 print(f"your total bill is ${bill}")  
