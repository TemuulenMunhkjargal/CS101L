########################################################################
##
## CS 101 Lab
## Program Assign_8.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : We’re going to work on something that is important to all students, grade weighting.
##           Our program will allow the user to enter 2 types of grades; Tests and Programs.
##           Each of our scores is assumed to be out of 100, so we only need the users score.
##           The tests are 60% of a student’sgrade, while the assignments are 40%.
##           In order to calculate the final score, we multiply the mean score of the tests by 0.6 and add it to the mean of assignments multiplied by 0.4.
##
## ALGORITHM : 
##      1. Main program starts in loop, and prints out menu with 8 options to choose from
##      2. After entering the corresponding letter or number for which option to run, it will loop back again, asking for another option
##      3. Will keep running until user hits q
## 
## ERROR HANDLING:
##      Display score for empty lists will show up as n/a
##      Can only enter an integer or a float value for each one of the options, cannot be lower than 0
##      7 and 8 as a user choice is not shown on the printed menu and is only for debugging purposes
##     
########################################################################

import math
Tests = []
Assignments = []


def score_Calc():
        sum1 = 0
        sum2 = 0
        stdSum1 = 0
        stdSum2 = 0
        if len(Tests) > 0:
            for score in Tests:
                sum1 += score
            meanTest = sum1 / len(Tests)
            for score in Tests:
                stdSum1 += (score - meanTest)**2
            stdTest = math.sqrt(stdSum1 / len(Tests))
            maxTest = max(Tests)
            minTest = min(Tests)
        else:
            meanTest = 'n/a'
            stdTest = 'n/a'
            maxTest = 'n/a'
            minTest = 'n/a'


        if len(Assignments) > 0:
            for score in Assignments:
                sum2 += score
            meanAssign = sum2 / len(Assignments)
            for score in Assignments:
                stdSum2 += (score - meanAssign)**2
            stdAssign = math.sqrt(stdSum2 / len(Assignments))
            maxAssign = max(Assignments)
            minAssign = min(Assignments)
        else:
            meanAssign = 'n/a'
            stdAssign = 'n/a'
            maxAssign = 'n/a'
            minAssign = 'n/a'
        if len(Assignments) > 0 and len(Tests) > 0:
            WeightedScore = (meanTest * 0.6) + (meanAssign * 0.4)
        else:
            WeightedScore = 0
        


        if len(Assignments) > 0 and len(Tests) > 0:
            print('{:<20}{:<10}{:<10}{:<10}{:<10}{}\n{}'.format('Type', '#', 'Min', 'Max', "Avg", 'STD', ('='*63)))
            print('{:<20}{:<10}{:<10}{:<10}{:<10.2f}{:.2f}'.format('Tests', len(Tests), minTest, maxTest, meanTest, stdTest))
            print('{:<20}{:<10}{:<10}{:<10}{:<10.2f}{:.2f}'.format('Programs', len(Assignments), minAssign, maxAssign, meanAssign, stdAssign))
            print("\nThe weighted score is ==> {:.2f}".format(WeightedScore))
        else:
            print('{:<20}{:<10}{:<10}{:<10}{:<10}{}\n{}'.format('Type', '#', 'Min', 'Max', "Avg", 'STD', ('='*63)))
            print('{:<20}{:<10}{:<10}{:<10}{:<10}{}'.format('Tests', len(Tests), minTest, maxTest, meanTest, stdTest))
            print('{:<20}{:<10}{:<10}{:<10}{:<10}{}'.format('Programs', len(Assignments), minAssign, maxAssign, meanAssign, stdAssign))
            print("\nThe weighted score is ==> {:.2f}".format(WeightedScore))

               


while True:
    print('{:^50}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format('Grade Menu', '1 - Add Test', '2 - Remove Test', '3 - Clear Tests', '4 - Add Assignment', '5 - Remove Assignment', '6 - Clear Assignments', 'D - Display Scores', 'Q - Quit\n'))
    userChoice = input('\n==> ')
    if userChoice == '1':
        try:
            userInput = float(input("Enter new Test score 0 - 100 ==> "))
            if userInput > 0:
                Tests.append(userInput)
            else:
                print("Test score must be more than 0")
        except:
            print('ERROR, invalid input')

    elif userChoice == '2':
        try:
            delChoice = float(input('Enter Test score to delete ==> '))
            if delChoice in Tests:
                Tests.remove(delChoice)
            else:
                print("Test score {} not found".format(delChoice))
        except:
            print('ERROR, invalid input')
     
    elif userChoice == '3':
            Tests.clear()

    elif userChoice == '4':
        try:
            userInput = float(input("Enter new Assignment score 0 - 100 ==> "))
            if userInput > 0:
                Assignments.append(userInput)
            else:
                print("Assignment score must be more than 0")
        except:
            print('ERROR, invalid input')
     
    elif userChoice == '5':
        try:
            delChoice = float(input('Enter Assignment score to delete ==> '))
            if delChoice in Assignments:
                Assignments.remove(delChoice)
            else:
                print("Test score {} not found".format(delChoice))
        except:
            print('ERROR, invalid input')

    elif userChoice == '6':
        Assignments.clear()      

    elif userChoice == 'Q' or userChoice == 'q':
        break              
    elif userChoice == 'D' or userChoice == 'd':
        score_Calc()
    elif userChoice == '7':
        print("DEBUGGING TEST\n", 'PRINTED LIST: ', Tests)

    elif userChoice == '8':
        print('DEBUGGING ASSIGNMENTS\n', 'PRINTED ASSIGN: ', Assignments)

    else:
        print('Please enter valid choice')