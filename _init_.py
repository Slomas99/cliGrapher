import random as r
import math as m
#python 3.6.2 lol
w=0
h=0
_list_ = []
numlist = []
def cls():
    print("\n"*100)
def process():
    try:
        for i in range(len(_list_)):
            for j in range(len(_list_[1])):
                if i == round(numlist[j]):
                    _list_[i][j]="█"
        print("█"*(w+2))
        for i in range(len(_list_)):
            app = ""
            for j in range(len(_list_[i])):
                app += str(_list_[i][j])
            print("█"+app+"█") #manage and print data
        print("█"*(w+2))
    except():
        print("Something went horribly wrong!")
cls()
while True:
    w, h = 100, 31;
    _list_ = [["-" for x in range(w)] for y in range(h)] #make blank list

    inp = input(">>> ")
    if inp == "help":
        print("""COMMANDS:\n
              help - displays list of all commands
              rand - displays random numbers onto graph
              pyramid - makes a pyramid like pattern
              sin - prints a premade sin function
              cos - prints a premade cos function
              tan - prints a premade tan function
              sinc - custom sin function
              
              """)
    if inp == "rand":
        numlist = []
        for i in range(len(_list_[4]) + 1):
            numlist.append(r.randint(1,(h+2))) #make random list of numbers
        process()
    if inp == "pyramid":
        numlist = [] #pyramids
        for j in range(25):
            for i in range(h):
                numlist.append(i)
            q = h
            while q > 0:
                numlist.append(q)
                q-=1
        process()
    if inp == "sin":
        numlist=[(h/2) for i in range(w+1)] #sin function
        for i in range(w+1):
            numlist[i] = (m.sin(i*37.5)+3)*5
        process()
    if inp == "cos":
        numlist=[(h/2) for i in range(w+1)] #cos function
        for i in range(w+1):
            numlist[i] = (m.cos(i*37.5)+3)*5
        process()
    if inp == "tan":
        numlist=[(h/2) for i in range(w+1)] #tan function
        for i in range(w+1):
            numlist[i] = (m.tan(i/12.5)+3)*5
        process()
    if inp == "sinc":
        fa = float(input("Enter your sin multiplier (default 37.5)\n>>> "))
        fb = float(input("Enter the Y modifier (default 3)\n>>> "))
        fc = float(input("Enter the final multipier (default 5)\n>>> "))
        numlist=[(h/2) for i in range(w+1)] #sine function
        for i in range(w+1):
            numlist[i] = (m.sin(i*fa)+fb)*fc
        process()
    if inp == "exp":
        numlist=[(h/2) for i in range(w+1)]
        for i in range(w+1):
            numlist[i] = i+i
        process()











