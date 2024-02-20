import re

def a(string):
    special_characters = re.compile(r'[^A-Za-z0-9\s]')
    return special_characters.search(string) is not None

def PasswordChecker(password):
    counter = len(password)
    if counter < 8:
        print("The password need to contain at least 8 characters")
    else:
        y = any(char.isupper() for char in password)
        z = any(char.islower() for char in password)
        o = any(char.isdigit() for char in password)
        d = a(password)
        if y and z and o and d:
             print("Strong")
        elif y and z and o:
            print("Strong but not the best")
        elif y and z:
            print("The password is mid")
        else:
            print("The password is weak")

print(PasswordChecker("214aA6B7&6"))