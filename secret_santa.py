# -*- coding: utf-8 -*-
                                        ####                                                          ####
                                        #                                                                #
                                        #  A small python program to generate a secret santa name draw,  #
                                        #  everyone is sent an email with the person to whom they are to #
                                        #  buy for. Probs not the most efficent code but IDGAF.          #
                                        #                                                                #
                                        # - SCOTTLB, 2016                                                #
                                        ####                                                          ####
import re, smtplib, random, sys


def prettyUIStuff():
    print("#########################################################")
    print("#                 --Python Secret Santa--               #")
    print("#                      By: SCOTTLB                      #")
    print("##########################2016###########################\n")


def inputNames(names, emailArr):
    #Get no of peeps
    noOfPeeps = input("Enter the amount of people in the draw: ")
    
    #Validate that shit
    while(noOfPeeps == "" or noOfPeeps <= 0):
        print("Data not valid; Try again")
        noOfPeeps = input("Enter the amount of people in the draw: ")
       
    
    for x in range(int(noOfPeeps)):
        
        tmpName = input("Enter the name of person " + str(x + 1) + ": ")
        while(tmpName == ""):
            print("Data not valid; Try again")
            tmpName = input("Enter the name of person " + str(x + 1) + ": ")
        names.append(tmpName)
                
        tmpEmail = input("Enter " + str(tmpName) + "'s email: ")
        emailArr.append(tmpEmail)
        

def scrambleArr(names, emailArr, namesShuffled, emailShuffled):
    
    z = zip(names, emailArr)
    
    random.shuffle(z)
    namesShuffled, emailShuffled = zip(*z)
    
    

def menu(names, emailArr, namesShuffled, emailShuffled, debug):
    print("\n-----ACTIONS-----")
    print("Normal Mode(1)\nTest Mode(2)\nSet Budget(3)\nExit(0)")
    
    choice = input("\nChoose your action: ")
    while choice not in {'1','2','3','4','999','0'}:
        choice = input("Invalid choice; please enter your choice again: ")
        
    if choice == '1':
        inputNames(names, emailArr)
        scrambleArr(names, emailArr, namesShuffled, emailShuffled)
        emailOut(namesShuffled, emailShuffled)
    elif choice == '2':
        print("DOESNT WORK")
        #debug = True
        #inputNames(names, emailArr)
        #scrambleArr(names, emailArr, namesShuffled, emailShuffled)
        #emailOut(namesShuffled, emailShuffled, debug)
    elif choice == '3':
        budget = input("Enter a budget: ")
        while(budget < 0 or budget == ""):
            budget = input("Enter a budget: ")
        print("Budget set to " + unichr(163) + budget)
        menu(names, emailArr, namesShuffled, emailShuffled, debug)
        
    elif choice == '0':
        sys.exit()
        
        
def emailOut(namesShuffled, emailShuffled, debug):
    
    #Gmail Settings
    EMAIL = "example@example.com"
    PWORD = "lamepassword"
    
    #Connect to gmail
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(EMAIL,PWORD)
    
    #Set email subject
    SUBJECT = "Sesh Dev 1 Secret santa draw! You've got a name!"
    
    #Because somehow this became a tuple
    namesShuffled  = list(namesShuffled)
    
    
    for x in range(len(namesShuffled)):
        #weird var assignment bullshit to make the list a 'circle'
        y = 0
        y = x + 1
        if(y == len(namesShuffled)):
            y = 0
            
        #set uo the main body of the message
        TEXT = 'Your Secret santa gift is going to: ' + namesShuffled[y] + '.\n The budget is: ' + budget
    
        #compose message
        msg = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
        
        #For every email address, send an email
        if debug == False:
            server.sendmail(EMAIL,emailShuffled[x],msg)
        else:
            print("TEST MODE: " + emailShuffled[x] + " is getting -> " + namesShuffled[y])
    
        
        
#### << ---------MAIN   ---------- >>
#Python version < 3 is a P.O.S.
input = raw_input
debug = False
budget = 10

#Constant Arrays
names = []
emailArr = []
namesShuffled = []
emailShuffled = []

#Run Methods
prettyUIStuff()
menu(names, emailArr, namesShuffled, emailShuffled, debug)