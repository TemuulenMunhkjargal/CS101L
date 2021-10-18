########################################################################
##
## CS 101 Lab
## Program Assignment_6.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : The Caesar Cipher is an encryption/decryption method that shifts the alphabet.  
##           For instance, if you have a cipher that shifts by 1, A would become B, B would become C, Z would wrap and become A.  
##           To decrypt that cipher you simply shift by -1.  
##           It is a very simple cipher that is easily broken.
##
## ALGORITHM : 
##      1. main() is called which is our whole program
##      2. The main() function runs in a while loop which will run Print_menu() and Get_input()
##      3. Depending on user choice either Encrypt() or Decrypt() will run
##      4. Since main program is in a loop steps 2-3 will repeat again until user enters Q (uppercase)
## 
## ERROR HANDLING:
##      1. Can only enter 1 2 or Q
##     
########################################################################


import string 

def Encrypt(string_text, int_key):     
    result = ""
    for i in range(len(string_text)):
      char = string_text[i]
      if (char.isupper()):
         result += chr((ord(char) + int_key - ord("A")) % 26 + ord("A"))
      elif char == ' ':
          result += ' '
      else:
         result += chr((ord(char) + int_key - ord("a")) % 26 + ord("a"))
    return (result)


def Decrypt(string_text, int_key):
    result = ''   
    for i in range(len(string_text)):
      char = string_text[i]
      if (char.isupper()):
         result += chr((ord(char) - int_key - ord("A")) % 26 + ord("A"))
      elif char == ' ':
        result += ' '
      else:
         result += chr((ord(char) - int_key - ord("a")) % 26 + ord("a"))
    return(result)

def Get_input():   
    selection = input("Enter your selection ==> ")
    return selection

def Print_menu():  
    print("MAIN MENU:\n1) Encode a string\n2) Decode a string\nQ) Quit")


def main():   
    Again = True   
    while Again:
        Print_menu()     
        Choice = Get_input()     
        if Choice == '1':       

            Plaintext = input("Enter (brief) text to encrypt: ").upper()       
            Key = int(input("Enter the number to shift letters by: "))      
            Ciphertext = Encrypt(Plaintext, Key)      
            print("Encrypted:", Ciphertext)     

        elif Choice == '2':       
            Ciphertext = input("Enter (brief) text to decrypt: ").upper()       
            Key = int(input("Enter the number to shift letters by: "))      
            Plaintext = Decrypt(Ciphertext, Key)      
            print("Decrypted:", Plaintext)

        elif Choice == 'Q':
            print("\nHave an ordinary day.")       
            Again = False 

        else:       
            print("\nWrong input\n")       
            continue

# our entire program: 
main() 
