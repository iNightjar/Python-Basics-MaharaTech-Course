# tuple is like an array .. or more like a vector
tuple = (1,2,3,4) # tuple with four elements
print(tuple)
tupe = tuple + (1,224,55,53) # indexing elements to the tuple
print(tupe) # printing new tuple

print(tupe[1:2])

# difference between string and tuple is the (,)
x = ('c')
y = ('c',)
print(type(x))
print(type(y))

# varaible swap
numberOne = 5
numberTwo = 6
(numberOne,numberTwo) = (numberTwo,numberOne)
firstTuple = (numberOne, numberTwo)
print(firstTuple)

# lists
list = [1,2,3]
# append to list
list.append(7)
print(list)

# userIndex List with appending values

indexList= []
while True:
    userInput = input("to append enter 'a'.\nto exit enter 'x'.\n")
    if userInput== 'a':
        userIndexValue = str(input("Enter value\n"))
        indexList.append(userIndexValue)
    else:
        print("Exiting program.\n")
        break
print("updated list: \n" , indexList)
print("\n *******************")

# extend list with listValues
indexList.extend([1,2,3,4,5,6,7,1,2,2,9.10])
# del element at specefic list
del(indexList[1] )
# pop() removes and returns the last item in the list

lastElementInList= indexList.pop()
print("last element in list is: ", lastElementInList)

# more operations in lists
string = " I <3 cs"
print(list(string)) # returns a list with every character forms

print(string.split())

print('_'.join(string))


listOfNumbers = [1,3,21,1,4,4,5,2]
print(sorted(listOfNumbers))

reversedList= listOfNumbers.reverse()
print(reversedList)

# list in memory
firstList = [1,2,3]
secondList = [1,2,3]
print(firstList, "the privious was listOne and the next is listTwo :" , secondList)
firstList[1] = 10
print(firstList, " after changing firstList[1] vlaue to > 10  && printing secondList too :" , secondList)
