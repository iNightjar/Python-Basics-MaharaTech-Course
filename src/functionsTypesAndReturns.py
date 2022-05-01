#!/bin/bash/python

# empty function with no parameters and return type
def printHello():
    print("we printed this through function with no parameters or return")
printHello()  # calling the function

# function with parameters
def printSum(firstNumber, secondNumber):
    print(firstNumber + secondNumber)
printSum(10,12)

# isEven one()
index=int(input("Enter number to check if it's Even\n"))
def isEven(index):
    return index%2==0
print(isEven(index))


# variable scope -- manupilating the value dependant on the scope of the variable secondNumber
def function(number):
        secondNumber = 1
        secondNumber += number
        print(secondNumber)
secondNumber = 5
function(10)
print(secondNumber)