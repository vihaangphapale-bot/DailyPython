str1 = input("Type something random: ")
str2 = input("Type something random again: ")
if len(str1) > len(str2):
    print(str1 , "Has more letters.")
elif len(str1) < len(str2):
    print(str2 , "Has more letters.")
else:
    print("They both have the same amount of letters.")

