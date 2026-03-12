name = input("Enter any name: ")
nameholder = set()
while name != "":
    if name in nameholder:
        print("Existing name.")
        break
    else:
        print("New name.")
        nameholder.add(name)
        name = input("Enter any name: ")    
for name in nameholder:
    print(name)