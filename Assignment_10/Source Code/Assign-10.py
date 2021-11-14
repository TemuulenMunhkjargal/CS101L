########################################################################
##
## CS 101 Lab
## Program Assign-10.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : In this Exam you will ask the user for a text file to read.
##           You’ll want to read all the words and output a count of the words that are used the most.  
##           ( We’ll only be concerned with words that have a length greater than 3 ) 
##
## ALGORITHM : 
##      1. Call function mainProcessing() which returns list
##      2. Pass list from mainProcessing() to function PrintDict(words)
##
## ERROR HANDLING:
##      Filename must be valid
##
########################################################################

import collections
characters = "!/,!-_."
wordDict = collections.defaultdict(list)

def PrintDict(Words):
    '''Takes a list and turns it into a dictionary with the amount a word occures as its key (integer).
    Then prints it out in a formatted fashion.'''
    for word in Words:
        wordCount = 0
        for i in range(len(Words)):
            if word == Words[i]:
                wordCount += 1
        if word not in wordDict[wordCount]:
            wordDict[wordCount].append(word)
        else:
            continue

    sortedKeys = sorted(wordDict.keys(), reverse=True)

    print("Most frequently used words")
    print("{:<30}{:<40}{:<30}\n{}".format("#", "Word", 'Freq', '='*74))
    count = 1
    for keys in sortedKeys:
        if (count > 10):
            break         
        for value in wordDict[keys]:
            print("{:<30}{:<40}{:<30}".format(count, value, keys))
            count += 1


def mainProcessing():
    '''Reads a file from user input, returns contents of the file in list format without special characters, and new lines.'''
    while True:
        try:
            fileName = input("Enter file name to open ==> ")
            with open(fileName, 'r') as file:
                readFile = file.readlines()
                words = []
            for row in readFile:
                words.append(row)
            break
        except (FileNotFoundError, FileExistsError, NameError):
            print('Could not open', fileName)

    unifiedString = ''
    for word in words:
        unifiedString += word.lower()
    for marks in characters:
        unifiedString = unifiedString.replace(marks, "")
    unifiedString = unifiedString.replace('\n', " ")
    DocumentedList = list(unifiedString.split())
    #The initial contents of the file was stored in a list, we turned it into a string and removed newlines,
    #special characters and lower cased every word. Then the string is appended to a list word by word 

    for word in DocumentedList:
        if(len(word) < 3):
            DocumentedList.remove(word)
    for word in DocumentedList:
        if(len(word) == 1):
            DocumentedList.remove(word)
    #There was an error in the first loop not removing 1 letter words so another loop was used again
    return DocumentedList


Words = mainProcessing()
PrintDict(Words)
