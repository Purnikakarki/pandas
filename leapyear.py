year=int(input("Enter a year"))
if(year % 400 == 0) and (year % 100!= 0):
    print("It is a leap year{year}")
else:
    print("It is not a leap year{year}.")
