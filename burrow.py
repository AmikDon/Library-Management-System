#this module does the burrowing process. A function is defined which asks the user his/her name and the Book ID he/she wants to burrow.
#If the user inputs invalid ID, then the program asks the user to input a valid ID.
#If the required book is not available, the program tells that the required book is not available.
#If the quantity of the book that the user require is more than the quantity available in the library,
#the program tells that there is only certain quantity of the required book is available.
#If the amount of book the user needs is available in the library,
#then the program modifies the value of the quantity of the book from the txt file(available books before –amount of the books the user took).
#Then the program asks the user if he/she wants to burrow more books.
#If the user wishes to burrow more books then the same process is done from the start.
#If the user does not want to burrow more books, then the function ends.import datetime

#f is defined to write the information of the burrowed book into a unique file
f = 1

#calling built in function datetime
import datetime
   
#defining a function which does burrowing process
def burrow():
    global f            #calling global variable f
    loop = False        

    success = False
    total = 0           #to sum up the amount
    now = datetime.datetime.now()       #putting the date and time in variable now.
    dic = {}    #creating an empty dictionary
    k=""        #storing empty string value in a variable k to add the name of the books

    while success == False:             # loop to enter proper name
        
        b = input("Enter your name:")   #name of the user stored in b.
        try:
            int(b)
            print("Enter a proper name!!!!")
            
        except:
            success = True

    while loop == False:                #loop to continue if the user wants to burrow more books.
        succes = True
        while success == True:          #loop to enter a proper book ID.
            try:
                a = int(input("Enter the Book ID you want to burrow:"))     #Desired Book ID stored in a.
                if 1 <= a <= 10:
                    success = False
                else:
                    print("Please enter a proper Book ID:")
            except:
                print("Please enter a valid value")

        while success == False:         #loop to enter a valid amount of books
            try:
                e = int(input("How many??"))    #quantity of the book desired stored in e
                success =True
            except:
                print("Enter a valid value")

        print("------------------------------------------------------------------------------")

        m = 1       #initializing m for key in dictionary

        #reading each line in file "books.txt" and storing value in dictionary dic.
        file1 = open("books.txt","r")
        for i in file1:
            c = i.replace("\n","")
            d = c.split(",")
            dic[m] = d
            m = m + 1


        #this while loop compares the Book ID given by the user with h. whose value keeps on increasing to 10.
        h = 1
        
        while h <= 10:
            if a == h:
                s = dic[h]      #putting the value of the required book id from a dictionary in a new list s.
                if int(s[2]) <= 0:  #comparing quantity of the books
                    print("Sorry we dont have it right now. It will available within few days.")
                elif int(s[2]) < e: #comparing quantity of the books
                    print("Sorry! We only have", int(s[2]) ," books right now!")
                else:
                    money = float(s[3].replace("$","")) * e     # calculating money by multiplying the quantity oof books with the price
                    total = total + money                       # adding all total price
                    remain = int(s[2]) - e      # subtracting the quantity of books available before with the quantity taken and storing in remain.
                    g = 1       # to compare the book ID with the input
                    
                    o = ""                      # to add the string values after the quantity is changed
                    file2 = open("books.txt","r")   #reading "books.txt"
                    for lin in file2:
                        if a == g:                  # if the book ID = g
                                            
                            x = lin.replace(s[2],str(remain))  #exchanging the quantity of the books with reamaining books
                            o = o + x   #adding up the information of the book in variable o.
                        else:
                            o = o + lin    #adding up the information of the book in variable o.
                        g = g +1    #increasing the value of g by 1.
                        file4 = open("books.txt","w")   #open file "books.txt"
                        file4.write(o)                  #writing the updated information in the file

                    while succes == True:       #to enter valid value(y/n)
                        try:
                            l = input("do you want to burrow more books??(y/n):")   #asking user if he/she whishes to continue or not and storing it in variable l.
                            print("------------------------------------------------------------------------------")
                            k = k + s[0] + ","  #adding up the name of the books
                            if l.lower() == "n":    #if user do not wish to continue

                                file = open("burrows"+str(f)+".txt","w")        #creating a new unique file
                                file.write(b +"," + k + str(now) +"," + "$"+str(total))     #writing the name of the burrower, name of the books, time and total amount of money to be paid.
                                f = f +1    #adding up f for unique filename

                                


                                   
                                print("Burrower's name:  " +b)
                                print("Name of the book:  " + k )
                                print("total amount:",total)
                                print("Time:"+now.strftime("%Y-%m-%d %H:%M:%S"))
                                print("------------------------------------------------------------------------------")
                                
                                    
                                loop = True             #changing the value of loop to True
                                succes = False          #changing the value of succes to False
                                h = h + 10              # adding h + 10 to end the loop
                                
                            elif l.lower() == "y":      #if user wishes to continue

                                
                                succes = False  #changing the value of succes to False

                            else:
                                print("please enter a proper value(y/n):")
                
                        except:
                            print("Please enter a proper value(y/n):")
                    
                    
                    
                                      
            h = h + 1       #adding h by 1 to chek another book ID
