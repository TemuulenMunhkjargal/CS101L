########################################################################
##
## CS 101 Lab
## Program #
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : Guess the users number based on the remainders
##
## ALGORITHM : 
##      1. Start by initializing 4 different lists that reset to empty each iteration of the loop
##      2.Take 3 inputs from user that contain the remainders left
##      3. Using a for loop check each number from 1 to 100 that fits the category
##      4. Each user entered number has an according list to it that contains all the numbers
##         that leave the remainders 
##      5. Using the set() and intersection() function we combine the same values from the 3 lists
##      6. Last final section that checks Y or N to continue the loop again or not 
##
## ERROR HANDLING:
##      If the algorithm can't find the number it asks for Y or N regardless
##      
##      First remainder can't be more than 3
## 
##      Input must be only Y or N at the end
##
##
########################################################################




check = ''

while check != 'N':
    list1 = []
    list2 = []
    list3 = []
    final_list = []
    user_input1 = int(input("What is the remainder when your number is divided by 3 ? "))
    if user_input1 > 2:
        print("The value entered must be less than 3")
        continue
    user_input2 = int(input('What is the remainder when your number is divided by 5 ? '))
    user_input3 = int(input("What is the remainder when your number is divided by 7 ? "))
    for i in range(1, 101):
        if i % 3 == user_input1:
            list1.append(i)
        if i % 5 == user_input2:
            list2.append(i)
        if i % 7 == user_input3:
            list3.append(i)
    final_list = set(list1).intersection(list2, list3)
    while True:
        if len(final_list) == 0:
            print("Sorry I couldn't find that number")
            break
        else:
            print("Your number was", *final_list)
            print("How amazing is that?\n")
            break
    while True:
        try:
            check = input("Do you want to play again? Y to continue, N to quit  ==> ")
            if check == 'Y' or 'N':
                break
            else:
                print("Wrong input")
        except ValueError:
            print("Please enter only Y or N")
            continue