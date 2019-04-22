#Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. 
user_ask = "Yes"
number_coins = -1

while user_ask == "Yes":
     number_coins += 1 
     user_ask = input("You have %d coins. \nDo you want another?" % number_coins)
print("No more for you.")