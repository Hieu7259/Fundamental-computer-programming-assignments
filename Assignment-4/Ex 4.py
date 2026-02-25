def lsit(numbers):
    totalnumbers = 0
    for addnumber in numbers:
        totalnumbers += addnumber
    return totalnumbers
testing = [18, 36, 67, 69, 911]
summa = lsit(testing)
print (summa)
