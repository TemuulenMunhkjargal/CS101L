########################################################################
##
## CS 101 Lab
## Program: Assignment-4.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : In this program you are going to simulate a slot machine in Pierson Hall.  
##           The slot machine has 3 reels and each reel will have numbers ranging from 1 to 10. 
##           The user can choose how many chips they start out with.  They are allowed to wager 
##           between 1 to the amount of bank they currently have on each spin.  If they match 3 
##           numbers, they will win 10 times their wager.  If they match 2 numbers they will win 3 times their wager.
##
## ALGORITHM : 
##      1. Program will start out with asking how much bank they want to start with
##      2. Next will ask how much they want to wager
##      3. Then it will calculate 3 reels from range 1-10 and depending on matching reels returns appropriate amount
##      4. Will run indefinitely until user runs out of bank
##      5. If user runs out of bank they can choose to play again and the entire program will loop again
## 
## ERROR HANDLING:
##      1. Wager not less than 0 or more than amount of bank
##      2. Bank cannot be less than 0 or more than 100
##      3. To play again only Y/Yes/YES/y/n/N/NO/No are accepted
##
##
########################################################################

import random


def play_again() -> bool:
    while True:
        answer = input("Do you want to play again? ==> Y/N ")
        if answer == 'Yes' or answer == 'YES' or answer == 'Y' or answer == 'y':
            return True
        elif answer == 'N' or answer == "No" or answer == "NO" or answer == 'n':
            print("\nThanks for playing.")
            return False
        else:
            print("Please enter YES/NO/Y/N")
            continue
        
def get_wager(bank : int) -> int:
    while True:
        wager = int(input("How much do you want to wager? ==> "))
        if wager > bank or wager <= 0:
            print("Please enter a value more than 0 or less than how much chips you have\n")
        else:
            return wager            

def get_slot_results() -> tuple:
    reel1 = random.randint(1, 10)
    reel2 = random.randint(1, 10)
    reel3 = random.randint(1, 10)

    return reel1, reel2, reel3

def get_matches(reela, reelb, reelc) -> int:
    if reela == reelb and reelb == reelc and reela == reelc:
        return 3
    elif reela == reelb and reelb != reelc or reela != reelc and reelb == reelc or reela == reelc and reelb != reela:
        return 2
    else:
        return 0

def get_bank() -> int:
    while True:
        chips = int(input("How many chips do you want to start out with? ==> "))
        if chips <= 1 or chips >= 101:
            print("Value must be higher than 1 or less than 101. Please enter valid input\n")
            continue
        else:
            return chips

def get_payout(wager, matches):
    if matches == 3:
        return wager * 10 - wager
    elif matches == 2:
        return wager * 2
    else:
        return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        spins = 0
        bank = get_bank()
        initial = bank
        most = [initial]

        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()
            spins += 1

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            most.append(bank)
            if bank <= 0:
                print("You lost all", initial, "in", spins, "spins")
                print("The most chips you had was", max(most))
                playing = play_again()
                break

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
