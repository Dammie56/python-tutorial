"""Leap year algorithm"""

year = int(input("Enter year:"))


if ((year % 4 == 0) and (year % 100 != 0)) or (
    (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0)
):
    print("It is a leap year")
else:
    print("It is not a leap year")

year = int(input("Enter the year here: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(True)
        else:
            print(False)
    else:
        print(True)
else:
    print(False)


year = int(input("Enter the year here: "))
if year % 4 == 0:
    print(True)
if year % 100 == 0:
    print(False)
if year % 400 == 0:
    print(True)
