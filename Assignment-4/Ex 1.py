addon = (input("Enter a number: "))
number = []
while addon != "":
    number.append(int(addon))
    addon = (input("Enter a number: "))
number.sort(reverse=True)
reverse_d = number[0:5]
print("The 5 greatest numbers are:", reverse_d)