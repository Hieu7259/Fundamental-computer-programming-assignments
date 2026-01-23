Talents = input('Enter Talents: ')
Pounds = input('Enter Pounds: ')
Lots = input('Enter Lots: ')
Total_weight = float(Talents) * 20 * 32 * 13.3  + float(Pounds) * 32 * 13.3 + float(Lots) * 13.3
Exact = int(Total_weight) // 1000
Clear = float(Total_weight) % 1000
print(f"The total weight in modern units is: {Exact} Kilograms and {Clear:.2f} Grams" )