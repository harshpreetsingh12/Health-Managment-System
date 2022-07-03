# health management system
# 3 clients- harry , rohan and hammad
#import datetime

def getdate():
    import datetime
    return datetime.datetime.now()
def logd(logc):
    # print("choose 1 for harry 2 for rohan 3 for hammad\n")
    # logc = int(input())
    # print(logc)
    if logc == 1:
        print("Enter your diet")
        diet = input()
        f = open("hms food/hdiet.txt", "a")
        f.write(f'\n Time = {getdate()} {diet} ')
        f = open("hms food/hdiet.txt", "r")
        # openr=openn.read()
        content = f.read()
        print(f'Harry your current diet is: = {content}\n')
    elif logc == 2:
        print("Enter your diet")
        diet = input()
        f = open("hms food/rdiet.txt", "a")
        f.write(f'\n Time = {getdate()} {diet} ')
        f = open("hms food/rdiet.txt", "r")
        # openr=openn.read()
        content = f.read()
        print(f'Rohan your current diet is: = {content}\n')
    elif logc == 3:
        print("Enter your diet")
        diet = input()
        f = open("hms food/hamdiet", "a")
        f.write(f'\n Time = {getdate()} {diet} ')
        f = open("hms food/hamdiet", "r")
        # openr=openn.read()
        content = f.read()
        print(f'Hammad your current diet is: = {content}\n')
def logex(loge):
    # print("choose 1 for harry 2 for rohan 3 for hammad\n")
    # logc = int(input())
    # print(logc)
    if loge == 1:
        print("Enter your exercise")
        exercise = input()
        fe = open("hms food/hex", "a")
        fe.write(f'\n Time = {getdate()} {exercise} ')
        fe = open("hms food/hex", "r")
        contente = fe.read()
        print(f'Harry your current exercises are: = {contente}\n')
    elif loge == 2:
        print("Enter your exercise")
        exercise = input()
        fe = open("hms food/rex.txt", "a")
        fe.write(f'\n Time = {getdate()} {exercise} ')
        fe = open("hms food/rex.txt", "r")
        # openr=openn.read()
        contente = fe.read()
        print(f'Rohan your current exercises are: = {contente}\n')
    elif loge == 3:
        print("Enter your exercise")
        exercise = input()
        fe = open("hms food/hamex", "a")
        fe.write(f'\n Time = {getdate()} {exercise} ')
        fe = open("hms food/hamex", "r")
        # openr=openn.read()
        contente = fe.read()
        print(f'Hammad your current exercises are: = {contente}\n')
def retex(rete):
    if rete == 1:
        fe = open("hms food/hex", "r")
        contente = fe.read()
        print(f'Harry your current exercises are: = {contente}\n')
    elif rete == 2:
        fe = open("hms food/rex.txt", "r")
        contente = fe.read()
        print(f'Rohan your current exercises are: = {contente}\n')
    elif rete == 3:
        fe = open("hms food/hamex", "r")
        contente = fe.read()
        print(f'Hammad your current exercises are: = {contente}\n')
def retd(retc):
    if retc == 1:
        fe = open("hms food/hex", "r")
        contente = fe.read()
        print(f'Harry your current diets are: = {contente}\n')
    elif retc == 2:
        fe = open("hms food/rex.txt", "r")
        contente = fe.read()
        print(f'Rohan your current diets are: = {contente}\n')
    elif retc == 3:
        fe = open("hms food/hamex", "r")
        contente = fe.read()
        print(f'Hammad your current diets are: = {contente}\n')

while(True):
    choice = input("you want to log or retrieve or exit\n")
    if choice == "log":
        print("You want to log:-> exercise or diet")
        logchoice=input()
        if logchoice=="diet":
            print("choose 1 for harry, 2 for rohan, 3 for hammad\n")
            logc = int(input())
            logd(logc)
        elif logchoice=="exercise":
            print("choose 1 for harry, 2 for rohan, 3 for hammad\n")
            loge = int(input())
            logex(loge)

    elif choice == "retrieve":
        print("You want to retrieve:-> exercise or diet")
        retchoice = input()
        if retchoice == "diet":
            print("choose 1 for harry, 2 for rohan, 3 for hammad\n")
            retc = int(input())
            retd(retc)
        elif retchoice == "exercise":
            print("choose 1 for harry, 2 for rohan, 3 for hammad\n")
            rete = int(input())
            retex(rete)
    elif choice=="exit":
        break