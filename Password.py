import getpass
def check(n, s):
    if len(n) != len(s):
        return False
    else:
        for i in range(0, len(n)):
            if n[i] != s[i]:
                return False
    return True

password = getpass.getpass("Please enter a password with numbers, symbols, and letters: ")

np = input("Could you please retype your passord? ")
w = True
while w:
    if check(password, np) == False:
        np = input("Wrong password. Please try again: ")
    else:
        print("Correct!")
        w = False
