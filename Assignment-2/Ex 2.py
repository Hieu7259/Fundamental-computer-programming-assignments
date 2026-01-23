cabinclass = input("Enter cabin class (LUX, A, B, C): ")
if cabinclass == "LUX":
        print("upper-deck cabin with a balcony")
elif cabinclass == "A":
        print("above the car deck, equipped with a window")
elif cabinclass == "B":
        print("windowless cabin above the car deck")
elif cabinclass == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")