year = int(input("Which year do you wanna check ?"))

leap_year = year % 4

not_leap_year = year % 100

century_leap_year = year % 400

if year % 4 == 0 :
    print("a leap year")
elif year % 100 == 0:
    print(" a leap year")
elif year % 400 ==  0:
    print("a leap year")
else:
    print("not a leap year")
