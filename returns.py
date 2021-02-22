#this module does the returnig process. A function is defined which asks the user his/her name and the Book ID he/she wants to return.
#If the user inputs invalid ID, then the program asks the user to input a valid ID.
#Then the program asks the user the quantity of books he/she wants to return.
#If the user inputs improper value, then the program asks the user to input a proper value.
#Then the program modifies the quantity of the book from the txt file(available books before + the amount of the books the user returned).
#Then the program asks the user if he/she wants to return more books. If the user wishes to return more books then the same process is done from the start.
#If the user does not want to return more books, then the function ends.


#f is defined to write the information of the returned book into a unique file
f = 1

#defining a function which does returning process
def returns():
    global f        #calling global variable f
    import datetime     #calling a built in function datetime

    
    dic = {}    #creating an empty dictionary
    k = ""
    
    
    
    loop = True
    success = False
    now = datetime.datetime.now()       #putting the date and time in variable now.
    
    while success == False:         #loop to enter proper name
        
        a = str(input("Enter your name:"))      #name of the user stored in a.
        try:
            int(a)
            print("Enter a proper name!!")
        except:
            success = True

    while loop == True:     #loop to continue if the ser wants to return more books
        while success == True:  #loop to enter a proper Book ID.
            
            try:
                b = int(input("Enter the Book ID you want to return:"))     #desired Book ID stored in b.
                if 1 <= b <= 10: 
                    success = False
                else:
                    print("Please enter a valid Book ID!")
            except:
                print("Please enter a valid value")



       
        while success == False:     #loop to enter a valid value
            try:
                d = int(input("How many?"))
                success = True
            except:
                print("Please enter a proper value")

        m =1        #initializing m for key in dictionary
        
        #reading each line in file "books.txt" and storing value in dictionary dic.
        file = open("books.txt","r")
        for i in file:
            c = i.replace("\n","")
            x = c.split(",")
            dic[m] = x
            m = m + 1

        
        
        s = dic[b]      #putting the value of required book id from a dictionaryy in a new list s.
        remain = int(s[2]) + d #adding the quantity of books available before with the quantity returned and storing in remain.
        o = ""      #to add string values after the quantity is changed.
        g = 1       # to compare the book ID with the input

        file2 = open("books.txt","r")  #open file "books.txt"               
        for line in file2:             #loop to read each line in file           
            if b == g:                 # If Book ID =g       
                h = line.replace(s[2],str(remain))      #exchanging the quantity of the books with remainng books
                o = o + h               #adding up the information of the book in variable o.
            else:
                o = o + line           # adding up the information of the book in variable o.
            g = g +1                    #increasing the value of g by 1.

        file4 = open("books.txt","w")   #open file "books.txt"
        file4.write(o)                  #writing the updated information in the file


        print("------------------------------------------------------------------------------")
        
        
        

        while success == True:  #starting a loop to enter a proper value
            try:
                e = str(input("Are there any other books you want to return??(y/n)"))   #asking user if he/she wants to continue or not and storing it in variable e.
                print("------------------------------------------------------------------------------")
                k = k + s[0] + ","
                if e.lower() == "n":    #if user do not wish to continue
                    file1 = open("returns"+str(f)+".txt","w")   #creating a new unique file
                    file1.write(a +"," + k +","+ str(now) +",")   #writing the name of the returner, name of the book and current date and time
                    f = f +1    #adding up f for unique filenames

                    print("Returner's name:" + a)
                    print("Name of the book:" + k)
                    print("Quantity of the book:",d)
                    print("Time:"+now.strftime("%Y-%m-%d %H:%M:%S"))
                    print("------------------------------------------------------------------------------")

        
                    loop = False        #changing the value of loop to False
                    success = False     #changing the value of success to False
                elif e.lower() == "y":  #if user wishes to continue
                     success = False
                else:
                    print("please enter a proper value(y/n):")
            
            except:
                 print("Please enter a proper value(y/n):")

        success = True      #changing the value of success to True
