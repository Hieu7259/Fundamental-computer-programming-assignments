name = input("Enter username: ")
word = input("Enter password: ")
wrongs = 0
while wrongs < 5:
    if name == "python" and word == "rules":
        print("Welcome")
        break
    else:
        wrongs += 1
        name = input("Enter username: ")
        word = input("Enter password: ")
        if wrongs == 5:
            print("Access denied")
      