# if conditional statements
number  = int(input(")Please enter an integer number:\n ")) # accepts integer numbers onlys
if number%2==0 :
    print(number , " is even number")
    print("if statemnt is executed")

elif number%3==0:
    print(number , " is odd number")
    print("else statement is executed")
print("end of program") # end of the program

# control flows
# while loops
# printing number until it equals 5
number=0 
while(number<5):
    print("the number is ", number )
    number += 1

#for loops , syntax > for var in range (stop value) : || for var in range(start, stop):

stopValue = int(input("Please limit to reach\n")) # note that the last printed value will be (stopValue -1 )
for iterativeVariable in range(stopValue):
    print("printed value is : ", iterativeVariable)
print('\n')


startValue = int(input("Please enter the starting point\n")) # note that the start value must be lower than the stop value
stopValue = int(input("Please enter the stop point\n")) # note that the last printed value will be (stopValue -1 )
for iterativeVaraible in range(startValue, stopValue):
    print("printed value is : ", iterativeVaraible)
print('\n')


# print the sum of printed iterative variables
startValue = int(input("Please enter the starting point\n")) # note that the start value must be lower than the stop value
stopValue = int(input("Please enter the stop point\n"))
sum = 0
for iterativeVaraible in range(startValue, stopValue):
    sum += iterativeVaraible
    print("printed value is : ", iterativeVaraible)
print('\nsum of printed values is :' , sum)


#he value of the iteration is attached to variable
startValue = int(input("Please enter the starting point\n")) # note that the start value must be lower than the stop value
stopValue = int(input("Please enter the stop point\n"))
increaser = int(input("Please enter increaser value\n"))
for iterativeVariable in range(startValue, stopValue, increaser):
    print("printed value is: ", iterativeVariable)
print('\n')

# Break Statement Example
sum = 0 
for iterationVariable in range(5,11,2):
    sum += iterationVariable
    if sum==5: 
        break # will break when sum =5
    print("sum is: ", sum)

#loop over string indexes
string = "abcdefgh"
for index in range(len(string)):
    print(index)

#loop over string by characters
string="abcdefgh"
for char in string:
    print(char)
