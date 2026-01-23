try:
    Year = int(input("Enter a year: "))
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                print("This year is a leap year")
            else:
                print("This year is not a leap year")
        else:
            print("This year is a leap year")
    else:
        print("This year is not a leap year")
except:
    print("Invalid year given")