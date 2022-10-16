import random


def montyhallgame():
    doors = [1, 2, 3]
    cardoor = random.choice(doors)
    doors.remove(cardoor)

    while True:
        userinput = input("Behind which door do you think the car is? 1, 2 or 3.")
        if userinput.isdigit():
            userinput = int(userinput)
            if 1 <= userinput <= 3:
                break
        else:
            print("Enter a valid door number, 1, 2, or 3.")

    #if player found the car
    if userinput == cardoor:
        announce = random.choice(doors)
        doors.remove(announce)
        left = doors[0]
        while True:
            decision = input(f"The host opens door {announce} for you and reveals a goat. Would you like to switch to door {left}? 'Y/N'")
            if (decision=="Y" or decision=="N"):
                break
            else:
                print(f"Press Y to switch to door {left} or N to stick to your initial decision")

        #if switching
        if decision=="Y":
            userinput = announce

    else:
        doors.remove(userinput)
        announce = doors[0]
        while True:
            decision = input(f"The host opens door {announce} for you and reveals a goat. Would you like to switch to door {cardoor}? 'Y/N'")
            if (decision == "Y" or decision == "N"):
                break
            else:
                print(f"Press Y to switch to door {cardoor} or N to stick to your initial decision")

        if decision=="Y":
            userinput = cardoor


    if userinput == cardoor:
        print("Congratulations! You won a car!")
    else:
        print("At least you are drinking fresh milk this winter!")


montyhallgame()

