########################################################################
##
## CS 101 Lab
## Program Assign_9.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : We are reading in crime data from a csv file, and our program will need to process various forms of data from the file.
##           We will need the amount of crimes comitted in months, zip codes and the crime with the highest # of offenses.
##
## ALGORITHM : 
##      1. Rread input from user to read which csv file to open and run
##      2. Read csv file and put input the information into a a list variable called lst, it is a listt with nested lists inside it, each nested list a row of the csv file
##      3. Find the month with the biggest amount of crimes and print it
##      4. Find the crime with the biggest amount of occurences
##      5. Ask user input for which offense to search by
##      6. Print out how many times that offense occured in the same zip code
## 
## ERROR HANDLING:
##      Accepts only valid filename
##      User inputs check if data exists
##     
########################################################################


import csv
MONTHS = {1: 'January', 2:'February', 3:"March", 4:'April', 5:'May', 6:'June', 7:'July', 8:'April', 9:'September', 10:'October', 11:'November', 12:'December'}

def readInFile(filename:str) -> list:
    '''reads the file into a list nested inside a list'''
    with open(filename, encoding='utf-8') as file:
        csvFile = csv.reader(file)
        lst = list(csvFile)
    return lst

def monthFromNumber(month: int) -> str:
    '''Returns month in form of string e.g(1 = January)'''
    if month not in range(1, 13):
        raise ValueError("Month must be 1-12")
    return MONTHS[month]

def createReportedDateDict(fileLst: list) -> dict:
    '''Returns a dictionary with the date as the key and # of crimes as the value'''
    result = {}
    for line in fileLst[1:]:
        date = line[1].strip()
        result[date] = result.get(date, 0) + 1

    return result

def CreateReportedMonthDict(fileLst: list) -> dict:
    '''Returns a dictionary with its key as the month of the offense and the value as how many times it occured'''
    result = {}
    for line in fileLst[1:]:
        month = int(line[1].split("/")[0].strip())
        result[month] = result.get(month, 0) + 1
    return result

def getTopTenValues(valueDict: dict) -> list:
    '''Returns a list with keys as its rows with its values as the top 10 items'''
    lst = list(valueDict.items())
    lst.sort(key = lambda x: x[1], reverse=True)
    return lst[:10]

def createOffenseDict(fileLst: list) -> dict:
    '''Returns a dictionary with a key as the offense, with the value as how many times it occurs'''
    result = {}
    for line in fileLst[1:]:
        offense = line[7].strip()
        result[offense] = result.get(offense, 0) + 1
    return result

def createOffenseByZip(fileLst: list) -> dict:
    '''Returns a dictionary with the key as the offense and the value as another nested dictionary, the nested
    dictionary has the zip code as a key and the value is how many times it occurs'''
    result = {}
    for line in fileLst[1:]:
        offense = line[7].strip()
        zipCode = line[13].strip()
        if offense not in result:
            result[offense] = {}
        result[offense][zipCode] = result[offense].get(zipCode, 0) + 1
        
    return result

if __name__ == '__main__':
    invalidFile = True
    while invalidFile:
        try:
            fileName = input("Enter the name of the crime data file ==> ")
            lst = readInFile(fileName)
            invalidFile = False
        except FileNotFoundError:
            print("Could not find file {}.".format(fileName))
    print()
    months = CreateReportedMonthDict(lst)
    top10months = getTopTenValues(months)
    print("The month with the highest # of crimes is {} with {} offenses".format(monthFromNumber(top10months[0][0]), top10months[0][1]))

    offenses = createOffenseDict(lst)
    top10offenses = getTopTenValues(offenses)
    print("The offense with the highest # of crimes is {} with {} offenses.".format(top10offenses[0][0], top10offenses[0][1]))
    
    offensesByZip = createOffenseByZip(lst)
    print()
    invalidKey = True
    while invalidKey:
        offenseKey = input("Enter an offense ==> ")
        if offenseKey in offensesByZip:
            invalidKey = False
        else:
            print("No valid offense found, try again.")

    print()
    print("{} offenses by zip code".format(offenseKey))
    print("{:20}{:10}".format('Zip Code', '# Offenses'))
    print('='*30)
    for key, value in offensesByZip[offenseKey].items():
        print("{:<20}{:>10}".format(key, value))

