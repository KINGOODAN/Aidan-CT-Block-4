'''
Program Goals:
    1. Get input from the user (at multiple points)
    2. We need to convert some of this input to INTs from STRs
    3. We need to provide choices to the user 
        a. Add more values to a list
        b. Return a value at a specific index
'''

import random
myList = []
def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""  1. Add to a list
    2. Add a bunch of numbers
    3. Add a few
    4. Return the value at an index position
    5. Random Search 
    6. Linear Search
    7. Print contents of list
    8. ExitProgram
     -- """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                addAFew()
            elif choice == "4":
                indexValues()
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                print(myList)
            else:
                break
        except:
            print("You made a whoopsie!")
    #TO ADD: 1. A way to loop the action, 2. A way to quit, 3.Think of repetition.

def addToList():
    print ("Adding to a list! Great choice!")
    newItem = input ("Type an integer here!" + "\n -- ")
    myList.append(int(newItem))

def addABunch():
    print ("We're gonna add a bunch of integers here!")
    numToAdd = input("How many new integers would you like to add?" + "\n -- ")
    numRange = input("And how high would you like these numbers to go?" + "\n -- ")
    for myList in range(0, int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is a new complete.")

def addAFew():
    while True:
        print("It seem that you want to add a few numbers!" + "\n -- ")
        whatNum = input("What numbers would you like to add if you are done type stop." + "\n -- ")
        myList.append(int(whatNum))
        if whatNum == ("stop"):
            return

def indexValues():
    print ("Ohhh! I eard you need a particular piece of data")
    indexPos = input("What index position are you curious about?" + "\n -- ")
    print(myList[int(indexPos)-1])

def randomSearch():
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're gonna check out each ietm ona at a time in your list! This sucks.")
    searchItem = input("What you lookin for, pardner?" + "\n -- ")
    for x in range(len(myList)):
        if myList [x] == (searchItem):
            print (f"Your item is at index position {x}")

if __name__ == "__main__":
    mainProgram()