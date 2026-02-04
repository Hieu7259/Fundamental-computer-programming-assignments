def middle(text):
    length = len(text)
    if length % 2 != 0:
        middle1 = length // 2
        return text[middle1]
    else:
        middle2 = length // 2 - 1
        middle3 = length // 2 + 1
        return text[middle2:middle3]
putin = input("Enter your words: ")
print(middle(putin))