sentence = "You may reach Mr. Atkinson through his office number: +842439999999 during work hours, or his cell phone number: 0987654321,"
words = sentence.split()
redacted_numbers = []
for word in words:
    clean_word = word.strip(",.!?")
    if (len(clean_word) == 10 and clean_word.isdigit()) or word.startswith("+84"):
        if word[-1] in ",.!?":
            redacted_numbers.append("[REDACTED]" + word[-1])
        else:
            redacted_numbers.append("[REDACTED]")
    else:
        redacted_numbers.append(word)
joined_numbers = " ".join(redacted_numbers)
print(joined_numbers)