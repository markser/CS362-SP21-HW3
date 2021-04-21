# to run the program
# python3 mark_ser_hw1.py
# then input year to check in console


def main():
    validInput = False
    while not validInput:
        try:
            userInputYear = int(input('Enter a year that is greater than 4: '))
            if userInputYear > 4:
                validInput = True
            else:
                print("Please enter a positive integer greater than or equal to 4")
        except ValueError:
            print("Please enter a integer ")

    # userInputYear = pos_num(int(input("Enter a year: ")))

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


if __name__ == "__main__":
    main()
