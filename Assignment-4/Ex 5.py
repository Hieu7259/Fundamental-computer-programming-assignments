def lsit(numbers):
    even_only = []
    for smth in numbers:
        if smth % 2 == 0:
            even_only.append(smth)
    return even_only
testing = [18, 36, 67, 69, 911]
no_odd = lsit(testing)
print(no_odd)