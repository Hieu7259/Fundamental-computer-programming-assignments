sentence = "Today is January 16, 2025. The temperature is 11 degrees Celsius."
words = sentence.split()
eliminate = [word.strip(",.") for word in words]
numbersum = 0
for number in eliminate:
    if number.isdigit():
        numbersum += int(number)
print("The sum of the numbers in the sentence above is:", numbersum)