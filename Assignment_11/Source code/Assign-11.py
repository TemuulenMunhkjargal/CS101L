########################################################################
##
## CS 101 Lab
## Program Assign-11.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : We’ll use our skills to create a clock class that can keeptrack of hours, minutes and seconds.   
##           The you should be able to create an instance with values for hour, minutes and seconds.  
##           You’ll want to make a new class with a __ini__ method.  You’ll want to set the attributes for hour, minute, and second in the init.
##
## ALGORITHM : 
##      1. Get input for the hour, minute and second parameters for the Clock class
##      2. Initiliaze the Clock class with clock and clock1
##      3. Ask user how much seconds to pass
##      4. Print the time n times (from step 3)
##
########################################################################


import time
class Clock():
    def __init__(self, hour = 0, minute = 0, second = 0, clockType = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.clockType = clockType

        if(self.second >= 60):
            self.second -= 60
            self.minute += 1

        if(self.minute >= 60):
            self.hour += 1
            self.minute -= 60


        


    def tick(self):
        self.second += 1

        if(self.second >= 60):
            self.second -= 60
            self.minute += 1

        if(self.minute >= 60):
            self.hour += 1
            self.minute -= 60


    def __str__(self):
        if(self.clockType == 0):
            if(self.hour >= 24):
                self.hour -= 24
            return ("{:02}:{:02}:{:02}".format(self.hour, self.minute, self.second))

        elif(self.clockType == 1):
            if(self.hour <= 11):
                return ("{:02}:{:02}:{:02} am".format(self.hour, self.minute, self.second))


            elif(self.hour == 0) or (self.hour == 24):
                return ("{:02}:{:02}:{:02} am".format(12, self.minute, self.second))


            elif(self.hour == 12):
                return ("{:02}:{:02}:{:02} pm".format(self.hour, self.minute, self.second))


            elif(self.hour >= 13) and (self.hour <= 23):
                tempHour = self.hour - 12
                return ("{:02}:{:02}:{:02} pm".format(tempHour, self.minute, self.second))



hour = int(input("Set the hour: "))
minute = int(input("Set the minute: "))
second = int(input("Set the second: "))

clock = Clock(hour, minute, second)
clock1 = Clock(hour, minute, second, 1)

timesToRun = int(input("How many seconds do you want to pass? ==> "))
for i in range(timesToRun + 1):
    print("")
    print(clock)
    print(clock1)
    clock.tick()
    clock1.tick()
    time.sleep(1)


