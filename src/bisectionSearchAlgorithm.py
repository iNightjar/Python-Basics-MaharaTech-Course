"""
Please think of a number between 0 and 100!
and the program should predict that number.
"""

lowNumber =int(input("Please enter  low number\n"))
highNumber = int(input("Please enter high number\n"))
print("Please think of a number between ", lowNumber  , " and " , highNumber , "  OK!\n")
confirmation = input('\n')
flag = False
if confirmation == "ok":
    while(lowNumber <= highNumber):
        middleNumber = int((lowNumber + highNumber)/2)
        print("is your secret key : ", middleNumber)
        index = input("Enter 'h' to indicate the guess is too high.\nEnter 'l' to indicate the guess is to low.\nEnter 'c' to indicate i guessed correctly\n")
        if (index=='c'):
            flag = True
            print("Game over. Your secrect number was : " + str(middleNumber))
            break
        else:
            if(index=='h'):
                lowNumber= middleNumber + 1
            else:
                highNumber = middleNumber -1

else:
    print("Exit program!. Bye Bye\n")