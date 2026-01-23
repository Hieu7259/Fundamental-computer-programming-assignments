def calculate_unit_price(diameter_cm, price_usd):
    radius = (diameter_cm / 2) / 100 #convert cm to m
    area = (radius ** 2) * 3.14
    unit_price = price_usd / area
    return unit_price

try:
    diameter = float(input("Enter the first pizza's diameter (cm): "))
    price = float(input("Enter the first pizza's price (USD): "))
    diameter2 = float(input("Enter the second pizza's diameter (cm): "))
    price2 = float(input("Enter the second pizza's price (USD): "))
    unitprice1 = calculate_unit_price(diameter, price)
    unitprice2 = calculate_unit_price(diameter2, price2)
    print(f"The unit price of the first pizza is: ${unitprice1:.2f} per m^2")
    print(f"The unit price of the second pizza is: ${unitprice2:.2f} per m^2")
    if unitprice1 < unitprice2:
        print("The first pizza provides better value for money.")
    elif unitprice1 > unitprice2:
        print("The second pizza provides better value for money.")
    elif unitprice1 == unitprice2:
        print("Both pizzas provide the same value for money.")
except:
    print("Invalid diamter or price given.")  