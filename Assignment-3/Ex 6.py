def acronym(phase):
    words = phase.split()
    acronym_letters = ""
    for word in words:
        acronym_letters += word[0].upper()
    return acronym_letters
bruh = input("Enter your phrase: ")
print(acronym(bruh))