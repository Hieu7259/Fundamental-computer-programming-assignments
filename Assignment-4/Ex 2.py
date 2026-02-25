number = int(input("Enter an integer number: "))
prime = True
for i in range(2, number):
    if number % i == 0:
        prime = False
        break
if prime == True:
    print("The number entered is a prime number")
else:
    print("The number entered is not a prime number")
