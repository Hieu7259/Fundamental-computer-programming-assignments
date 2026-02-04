smallest = None
largest = None
number = input("Enter a number: ")
while number != "":
    number = float(number)
    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number
    number = input("Enter a number: ")
    if number == "":
        print("The smallest number is:", smallest)
        print("The largest number is:", largest)
        break