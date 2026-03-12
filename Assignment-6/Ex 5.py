def remove(numbers):
    no_odd = []
    for any in numbers:
        if any % 2 == 0:
            no_odd.append(any)
    return no_odd
testing = [1, 2, 3, 4, 5]
no_odd = remove(testing)
print("The original list is:", testing)
print("The cut-down list is:", no_odd)
