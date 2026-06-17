import random

amount = 0
while True:
    amount = input("How much money would you like to deposit? $")
    if amount.isdigit():
        amount = int(amount)
        if amount > 0:
            break
        else:
            print("Please choose a number greater than 0.")
    else:
        print("ERROR Please try again.")

gh = ""
while gh == "":
    lines = "hi"
    while True:
        lines = input('''Choose a number 1-3 to bet on rows:
    1 Line  = Top Row
    2 Lines = Top + Middle Rows
    3 Lines = Top + Middle + Bottom Rows ''')
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= 3:
                break
            else:
                print("Please choose a number that is 1 to 3.")
        else:
            print("ERROR Please try again.")

    bet = 0
    while True:
        bet = input("How much money would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                if bet * lines > amount:
                    print("You do not have enough money to bet. Please try again.")
                else:
                    break
            else:
                print("Please choose a number greater than 0.")
        else:
            print("ERROR Please try again.")

    if input("Would you like to spin the wheel or quit(enter to spin)? ") == "":
        amount -= bet * lines
        hi = ['V', 'I', 'P']
        for i in range(0, 3):
            a = random.choice(hi)
            b = random.choice(hi)
            c = random.choice(hi)
            print(a, '|', b, '|', c)
            if a == b and b == c:
                if i + 1 <= lines:
                    amount += bet
        print("Your balence is now $" + str(amount))

    gh = input("Would you like to spin the wheel again(enter for yes)? ")

print("Thanks For Playing!")