def uppercase_course_code(course_code):
    if len(course_code) == 5 or 6:
        letters_only = course_code[:-3]
        digits_only = course_code[-3:]
        if letters_only.isalpha() and letters_only.isupper() and digits_only.isdigit() and len(digits_only) == 3:
            return True
    else:
        return False
test_code = "TEC001"
if uppercase_course_code(test_code):
    print("true")
else:
    print("false")
