########################################################################
##
## CS 101 Lab
## Program: GradeCalculator.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
## Date: Fall 2021
## PROBLEM : Calculate grades based on a weight system
## 
## ALGORITHM : 
##      1. Take inputs for lab, exam and attendance grades from user
##      
##      2. Pass those variables to two different functions to calculate
##         the weighted grade and letter grade
##      3. Print results
##
## ERROR HANDLING:
##      If input is more than 100 or 0, it automatically sets the input to 100 or 0.
##      Inputs take float type
##
########################################################################


def calculate_grade(labs, exam, attendance):
    weighted_grade = (exam * 0.2) + (labs * 0.7) + (attendance * 0.1)
    return weighted_grade

def get_letter_grade(grade):
    if grade >= 90 and grade <= 100:
        letter_grade = 'A'
    elif grade >= 80 and grade <= 89:
        letter_grade = 'B'
    elif grade >= 70 and grade <= 79:
        letter_grade = 'C'
    elif grade >= 60 and grade <= 69:
        letter_grade = 'D'
    elif grade >= 0 and grade <= 59:
        letter_grade = 'F'
    return letter_grade

## Main program
print("**** Welcome to the LAB grade calculator! ****")
userName = input("\nWho are we calculating grades for? ==> ")
lab_grade = float(input("\nEnter the LABS grade? ==> "))
if lab_grade > 100:
    print("The lab value should have been 100 or less. It has been changed to 100.")
    lab_grade = 100
elif lab_grade < 0:
    print("The lab value should have been 0 or greater. It has been changed to 0.")
    lab_grade = 0
exam_grade = float(input("\nEnter the EXAMS grade> ==> "))
if exam_grade > 100:
    print("The exam value should have been 100 or less. It has been changed to 100.")
    exam_grade = 100
elif exam_grade < 0:
    print("The exam value should have been 0 or greater. It has been changed to 0.")
    exam_grade = 0
attendance_grade = float(input("\nEnter the Attendance grade? ==> "))
if attendance_grade > 100:
    print("The attendance value should have been 100 or less. It has been changed to 100.")
    attendance_grade = 100
elif attendance_grade < 0:
    print("The attendance value should have been 0 or greater. It has been changed to 0.")
    attendance_grade = 0

weighted_grade = calculate_grade(lab_grade, exam_grade, attendance_grade)
letter_grade = get_letter_grade(weighted_grade)
print("\nThe weighted grade for {} is {:.1f}\n{} has a letter grade of {}".format(userName, weighted_grade, userName, letter_grade))
print("\n**** Thanks for using the Lab grade calculator ****")
