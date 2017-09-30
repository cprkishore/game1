#!/usr/bin/python

import random
import subprocess
import os
import datetime
import sys
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def cls():
        os.system('clear')

def sum(arg1,arg2):
        total = arg1 + arg2
        print "############"
        print "Total is:",total
        print "############"
        return;

def startgame():
        if (int(level) == 1):
                repeat = 'y'
                while repeat.lower() in ('y','yes'):
                        cls()
                        a = random.randint (0, 10)
                        b = random.randint (0, 10)
                        c = a + b
                        print ("Add %d + %d" % (a, b))
                        try:
                                s = int(raw_input ("And enter the sum here:"))
                                if (c == s):
                                        print bcolors.OKGREEN + "Your Answer is CORRECT" + bcolors.ENDC
                                else:
                                        print bcolors.FAIL + "Sorry WRONG Answer" + bcolors.ENDC
                        except ValueError:
                                print bcolors.WARNING + "invalid data, please enter the answer as integers only" + bcolors.ENDC
                        repeat =  raw_input("continue Level1?(y/n):" )
                        while repeat.lower() not in ('y','yes','n','no'):
                                print "choose y/n"
                                repeat =  raw_input("continue Level1?(y/n):" )
                                                                                            
        elif (int(level) == 2):
                repeat = 'y'
                while repeat.lower() in ('y','yes'):
                        cls()
                        a = random.randint (11, 99)
                        b = random.randint (11, 99)
                        c = a + b
                        print ("Add %d + %d" % (a, b))
                        try:
                                s = int(raw_input ("And enter the sum here:"))
                                if (c == s):
                                        print bcolors.OKGREEN + "Your Answer is CORRECT" + bcolors.ENDC
                                else:
                                        print bcolors.FAIL + "Sorry WRONG Answer" + bcolors.ENDC
                        except ValueError:
                                print "invalid data, please enter the answer as integers only"
                        repeat =  raw_input("continue Level2?(y/n):" )
                        while repeat.lower() not in ('y','yes','n','no'):
                                print "choose y/n"
                                repeat =  raw_input("continue Level2?(y/n):" )


        elif (int(level) == 3):
                repeat = 'y'
                while repeat.lower() in ('y','yes'):
                        cls()
                        print "THIS WILL DISPLAY TOTAL OF TWO NUMBERS (numbers only)"
                        try:
                                arg1 = int (raw_input ("Enter first number:"))
                                arg2 = int (raw_input ("Enter Second number:"))
                                sum(arg1,arg2)
                        except ValueError:
                                print "invalid data, please enter the first number and second number as integers only"
                        repeat =  raw_input("continue Level3?(y/n):" )
                        while repeat.lower() not in ('y','yes','n','no'):
                                print "choose y/n"
                                repeat =  raw_input("continue Level3?(y/n):" )

        else:
                cls()
                print "XXXXXXXXXXXXXXXXXXX"
                print "Choose 1,2,3, or 4"
                print "XXXXXXXXXXXXXXXXXXX"


############### MAIN #############       
cls()
quit = 'n'               
again = 'y'
while again.lower() in ('y','yes'):
        cls()
        print """
                
       ,==;,
       )a,a\g
       \=_/8
       _| (_3,
      /(__/\]\
     (_,,__) \\
     //\  ;/  \\ 
    //  )__\   \|_
  _'/  |[]__L,  ,>}
/t}  / ,   [| 
6    /-.|=._|/
    /  .'`-/`
   ( .' | /
   \ |  ( |
    \_)  \_).
     \ \  \ |
      \ >  >|
snd /.'  / /
         '-'

                                
                
                """
        print bcolors.HEADER + "###Enter 1 for LEVEL1###" + bcolors.ENDC
        print bcolors.HEADER + "###Enter 2 for LEVEL2###" + bcolors.ENDC
        print bcolors.HEADER + "###Enter 3 for LEVEL3###" + bcolors.ENDC
        print bcolors.HEADER + "###Enter q for Quit###" + bcolors.ENDC
        try:
                level = raw_input ("Choose option?:")
                if level.lower() in ('q','quit'):
                        again = 'n'
                elif (1<= int(level) <= 3):
                        startgame()
                else: 
                        print "XXXXXXXXXXXXXXXXXXXXXX"
                        print "choose 1,2,3 or q only"
                        print "XXXXXXXXXXXXXXXXXXXXXX"
                        wait = raw_input("#Click enter to go back to the main screen:")
                        again = 'y'
        except ValueError:
                print "Please Choose 1,2,3, or q"
                wait = raw_input("##Click enter to go back to the main screen:")
                again = 'y'

else:
        if again.lower() in ('n','no'):
                cls()
                print "Have a good Day, BYE"
