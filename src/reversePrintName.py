#!/usr/bin/python
n=input("Enter Your Name\n")
print(n[::-1]) # same as the below statement
for i in range(len(n)-1, -1 , -1 ): # reverse looping letters and print them 
     print(n[i],end="")
print('\n')
