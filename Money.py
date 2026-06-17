amount = 0
add = 0
while True:
    wd = input("Would you like to withdrawl some money or deposit some money(w/d)").lower()
    if wd == 'w':
        add = int(input("How much would you like to withdrawl? $"))
        amount -= add
        print("You have a total of $" + str(amount))
        add = 0
    elif wd == 'd':
        add = int(input("How much would you like to deposit? $"))
        amount += add
        print("You have a total of $" + str(amount))
    else:
        print("ERROR")