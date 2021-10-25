########################################################################
##
## CS 101 Lab
## Program Assignment_7.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : In this lab we’ll write a program to read through a file containing information about fuel economy and output the results to a file above a threshold that the user gives.  
##           If the user wants to see all vehicles with a combined mpg greater than 50, then yourprogram will output that information to the file of their choosing.
##
## ALGORITHM : 
##      1. The functions get_MPG(), get_InputFile() and get_OutputFile() are called in that order, they all return a single value and are stored in a variable in the main code.
##      2. The values from get_MPG() and get_InputFile() are passed to readInput(str, int)
##      3. readInput() will run and return 2 values which are both lists
##      4. The 2 returned lists will run in the main program and will write to the output file
## 
## ERROR HANDLING:
##      Your program will need to ask the user for a minimum fuel economy, and be able to handle non float data being entered.  It should continually ask for a correct value.  
##      It should also make sure they don’t enter a value less than or equal to zero or greater than 100.  The program will ask for an input file and should loop until the user 
##      gives a valid file that can be opened.  It should also ask for an output file.  While a FileNotFoundError won’t be thrown trying to open a file in write mode, 
##      it can generate an IOError.
##  
##      Your program should also be able to handle an incorrect combinedmpg column as in vehicles2.txt.  
##      When a bad value that can’t be converted is encountered, you should warn the user and give the year, make and model that had the error.
##     
########################################################################

from os.path import exists


def get_MPG():
    flag = 0
    while flag == 0:
        try:
            mpg = float(input("Enter the minimum mpg ==> "))
            if mpg < 0 or mpg > 100:
                print("Please enter a number more than 0 or more than 100")
                continue
            flag = 1
            return mpg

        except:
            print("Enter a number only")
            continue


def get_InputFile():
    flag = 0
    while flag == 0:
        try:
            getInputFile = input("Enter the name of the input file ==> ")
            if exists(getInputFile):
                return getInputFile
            else:
                print("Could not find file", getInputFile)
                continue
        except:
            print("Invalid input")
            continue

def get_OutputFile():
    flag = 0
    while flag == 0:
        try:
            getOutputFile = input("Enter the name of the output file ==> ")
            if exists(getOutputFile):
                return getOutputFile

            else:
                print("Could not find file", getOutputFile)
                continue
        except:
            print("Invalid input")
            continue


def readInput(inputfile, mpg):
    data = []
    processedData = []
    processedCars = []
    ErrorValue = []
    ErrorCar = []
    finalList = []
    Errors = []
    with open(inputfile, 'r') as file:
        placeholder = file.readline()
        data = file.readlines()

    for info in data:
        processedData.append(info.strip().split('\t'))

    for info in range(len(processedData)):
        try:
            if float(processedData[info][7]) > float(mpg):
                processedCars.append(processedData[info])
        except ValueError:
            ErrorValue.append(processedData[info][7])
            ErrorCar.append(processedData[info])

    if ErrorValue:
        print('')
        for cars in range(len(ErrorValue)):
            Errors.append(("Could not convert value {} for vehicle {} {} {}".format(ErrorValue[cars], ErrorCar[cars][0], ErrorCar[cars][1], ErrorCar[cars][2], ErrorCar[cars][7])))

    for cars in range(len(processedCars)):
        finalList.append(("{} {:<20}{:<40}{:>10.2f}".format(processedCars[cars][0], processedCars[cars][1], processedCars[cars][2], float(processedCars[cars][7]))))

    return finalList, Errors






mpg = get_MPG()
file = get_InputFile()
outputFile = get_OutputFile()
cars, errors = readInput(file, mpg)

if errors:
    print('')
    for error in errors:
        print(error)

with open(outputFile, 'w') as file:
    for car in cars:
        file.write(car)
        file.write('\n')
