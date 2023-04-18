'''
Created on Oct 2, 2022

@author: Brandon Demeritt
'''

heightCounter = 0

baseWidth = int(input("Please enter the base width of the arrow:\n"))
arrowHeight = int(input("Please enter the height of the arrow:\n"))
headWidth = int(input("Please enter the width of the arrow head:\n"))

while headWidth <= baseWidth:
    headWidth = int(input("Sorry, please enter a head width larger than the base width:\n"))

while heightCounter < arrowHeight:
    print("")
    heightCounter += 1
    baseIndex = 0
    while baseIndex < baseWidth:
        print("*", end="")
        baseIndex += 1

decreasingNum = int(headWidth)
print("")

while decreasingNum > 0:
    headCounter = 0
    while headCounter < headWidth:
        print("*", end="")
        headCounter += 1
    print("")
    decreasingNum -=1
    headWidth -= 1
