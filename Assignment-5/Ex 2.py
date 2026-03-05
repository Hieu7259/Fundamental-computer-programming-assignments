def hexcolor(color_code):
    if color_code[0] != '#':
        return False
    if len(color_code) != 7:
        return False
    for character in color_code[1:]:
        if character not in '0123456789ABCDEFabcdef':
            return False
    return True
test_code = "#1A2B3C"
if hexcolor(test_code):
    print("True")
else:
    print("False")