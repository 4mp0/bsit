import random, os

clear = lambda: os.system('cls')

ansArray = [
        "You passed the exam",
        "You failed the exam",
        "She's not the one",
        "She's the one",
        "Stay strong",
        "Forget that shit",
        "Fuck it"
    ]

def rndmQ():
    x = len(ansArray) - 1
    print(ansArray[random.randint(0,x)])

def usr():
    usrInput = input("Type 'yes' to test your luck again! 'no' to quit\n").lower()
    clear()
    if usrInput == "yes" or usrInput == "y":
        rndmQ()
        usr()
    if usrInput == "no" or usrInput == "n":
        print("See you next time!")
        exit()
    else:
        usr()
        
def main():
    print("Running!")
    clear()
    rndmQ()
    usr()
main()