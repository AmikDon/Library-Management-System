## defining a function to read the information of the books available from the txt file
def read():
    print("==========================Library Management System==========================")
    print("------------------------------------------------------------------------------")
    print("Book ID    Name            Author     Quantity   Price")
    print("------------------------------------------------------------------------------")

    # opening the txt file to read
    file = open("books.txt","r")
    
    n = 1                                           # setting n = 1 for unique Book ID
    m = 1                                           # m is the key of the dictonary

    # starting a for loop to display the books available
    for line in file:
        print(" ",n,"\t" + line.replace(",","\t"))
        n = n + 1                                   # increasing the value of Book ID by 1.


