#This is the main module. In this moduule all the modules are called to perform its corresponding tasks.

import datetime     #calling built in function datetime


succes = True       #initializing succes = True

while succes == True:   #loop to exit only if the user wishes to do so
    import read
    read.read()
    print("------------------------------------------------------------------------------")
    
    print("Press 1 to burrow")
    print("Press 2 to return")
    print("Press 3 to exit")
    print("------------------------------------------------------------------------------")

    b = False
    while b == False:   #loop to enter proper value
        try:
            a = int(input())    #takes input from the user and stores in variable a.
            b = True
        except:
            print("please enter a proper value")



    if a == 1:          #if user whishes to burrow
        import burrow   #calls burrow module
        burrow.burrow() #calls burrow() function from burrow module

    elif a == 2:        #if user wishes to return

        import returns  #calls returns module
        returns.returns()   #calls returns() function from returns module
    elif a ==3:         #if user wishes to exit
        succes = False  #change the value of succes to False.
        
    else:
        print("please enter a proper value(1/2/3):")

