#First problem--Using a while loop, print out the numbers between 1 and 10 inclusive.
#Same as the previous problem, except you will prompt the user for the number to start on and the number to end on.

num_start = int(input("Please enter a starting number: "))
num_end = int(input("Please enter an ending number: "))

while num_start <= num_end:
    num_start += 1
    print (num_start)