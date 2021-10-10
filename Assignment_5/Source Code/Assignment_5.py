########################################################################
##
## CS 101 Lab
## Program Assignment_5.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : The Linda Hall library wants to come up with a new library card numbering system for students.  
##          The card number’s first 5 characters are A-Z, which will normally be the first five characters of the student’s name.  
##          The next character at index 5is a string value either 1, 2, or 3 
##          which represents the different schools; SCE, School of Law, or College of arts and Sciences.  
##           The character at index 6 is either 1, 2, 3, or 4.  These are the grade levels; 
##           Freshman, Sophomore, Junior, and Senior. The next 2 characters are 0-9, and the last character at index 9 is the check 
##           digit to verify the previous values.  The last character is also 0-9.
##
## ALGORITHM : 
##      1. Enter library card ID as string from user input.
##      2. Library Card ID gets passed to verify_check_digit function to check for errors.
##      3. If verify_check_digit returns true the card is valid and asks user again for ID card until they hit enter.
##          Else if its returns false writes out what error it caused. Asks again for ID card until they hit enter.
## 
## ERROR HANDLING:
##      1. The first 4 indexes must be letters A-Z
##      2. The last 3 indexes must be numbers 0-9
##      3. The 6th element must be 1, 2 or 3
##      4. The 7th element must be 1, 2, 3 or 4
##      5. From index 0-8 using the formula (index + 1) * value; the modulus of 10 of the sum of those values must be
##         equal to the last value in index 9
##      6. ID card string length not less or more than 10
########################################################################


import string


def character_value(str) :
    ''' Returns 0 for A, 1 for B, etc. '''
    for chr in str:
        return string.ascii_uppercase.index(chr)


def get_check_digit(str) :
    ''' Returns the check digit for the name and sid. '''
    stringSum = 0
    numSum = 0
    for char in str[:5]:
        stringSum += (str.index(char) + 1) * character_value(char)
    for num in str[5:9]:
        numSum += (str.index(num) + 1) * int(num)
    return (stringSum + numSum) % 10


def verify_check_digit(str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    str = str.upper()
    firstHalf = str[:5]
    secondHalf = str[7:]
    if len(str) != 10:
        return False, "The length of given number must be 10"
    elif firstHalf.isalpha() == False:
        pos = 0
        error = ''
        for letter in firstHalf:
            if letter.isalpha() != True:
                error = letter
                break
            pos += 1
        return False, "The first five characters must be A-Z, the invalid character is at {} is {}".format(pos, error)
    elif secondHalf.isnumeric() == False:
        pos = 7
        error = ''
        for letter in secondHalf:
            if letter.isnumeric() != True:
                error = letter
                break
            pos += 1
        return False, "The last 3 characters must be 0-9, the invalid character is at {} is {}".format(pos, error)
    elif int(str[5]) > 3:
        return False, "The sixth character must be 1, 2 or 3"
    elif int(str[6]) > 4:
        return False, "The seventh character must be 1, 2, 3, or 4"
    elif get_check_digit(str) != int(str[9]):
        return False, "Check digit {} does not match calculated value {}".format(str[9], get_check_digit(str))
    else:
        return True, ''


def get_school(str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    if int(str[5]) == 1:
        return "School of Computing and Engineering SCE"
    elif int(str[5]) == 2:
        return "School of Law"
    elif int(str[5]) == 3:
        return "College of Arts and Sciences"
    else:
        return "Invalid School"
    
  

def get_grade(str):
    if int(str[6]) == 1:
        return "Freshman"
    elif int(str[6]) == 2:
        return "Sophomore"
    elif int(str[6]) == 3:
        return "Junior"
    elif int(str[6]) == 4:
        return "Senior"
    else:
        return "Invalid School"
   

if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)
    while True:

        print()
        card_num = input("Enter Library Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
