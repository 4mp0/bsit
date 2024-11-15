import os, json
clear = lambda: os.system("cls")
clear()

qtsData = {}
ansData = {}

def helpFunc():
    clear()
    print("""
            questions-----input questions for the reviewer\n
            answers-------input answers for the reviewer\n
            reviewer------use the reviewer\n
            clear---------clear console""")
    main()

def revFunc():
    clear()
    tmp: int = 0
    score: int = 0
    while tmp < len(qtsData):
        usrInput: str = str(input(f"""\nScore: {score}\nQ: {qtsData.get("key"+str(tmp))}\nAnswer: """))
        if usrInput != ansData.get("key"+str(tmp)):
            print("Incorrect!")
        else:
            score += 1
            print("Correct!")
        tmp+=1
    main()

def qtsFunc() -> str:
    clear()
    usrInput: str = str(input("Import Questions:")).split(",")
    tmp: int = 0
    while tmp < len(usrInput):
        qtsData["key"+str(tmp)] = usrInput[tmp]
        tmp+=1
    main()

def ansFunc() -> str:
    clear()
    usrInput: str = str(input("Import Answers:")).split(",")
    tmp: int = 0
    while tmp < len(usrInput):
        ansData["key"+str(tmp)] = usrInput[tmp]
        tmp+=1
    main()

def clr(): clear();main()

def main():
    clear()
    func: dict = {"help":helpFunc,"review":revFunc,"questions":qtsFunc,"answers":ansFunc,"clear":clr}
    usrInput = input("Type questions, answers, review, help: ").lower()
    func.get(usrInput, helpFunc)()
main()
