year = int(input("Enter your year here: "))
if year % 4 == 0:
    print(True)
if year % 100 == 0:
    print(False)
if year % 400 == 0:
    print(True)
else:
    print(False)
