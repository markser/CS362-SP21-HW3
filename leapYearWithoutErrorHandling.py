# to run the program
# python3 mark_ser_hw1.py
# then input year to check in console


userInputYear = int(input("Enter a year: "))

if (userInputYear % 4) == 0:
   if (userInputYear % 100) == 0:
       if (userInputYear % 400) == 0:
           print(str(userInputYear) + " is a leap year")
       else:
           print(str(userInputYear) + " is not a leap year")
   else:
       print(str(userInputYear) + " is a leap year")
else:
   print(str(userInputYear) + " is not a leap year")



