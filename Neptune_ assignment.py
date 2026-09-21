#Neptune Group Members
#Brenda Ramba Kade, Mugazhu Paul Kakono, Atukunda Valeline Alina, Namazzi Kizza Josephine, Nakiyimba Joy
#Library Book Borrowing Desk Assignment
#first  we define a new function for no of days and the type of book
def max_no_of_days(type_of_book):
    if type_of_book == "Textbook":
        return 14
    elif type_of_book == "Novel":
        return 7
    elif type_of_book == "Reference":
        return 2
    else:
        return 0
#then we define a function for the which year of study can borrow a specific book
def which_year_can_borrow_reference(year):
    if year == 3 or year == 4:
        return True
    else:
        return False
# Here we create the original counters
textbooks = 0
novels = 0
references = 0
successful = 0
try :
    n=int(input("Enter the number of borrowing transcations to be processed: "))
except ValueError:
    print("Please enter a valid number of transcations to be processed.")
    #the n tells Python how many times to run the loop and n=0 is to create a fallback value incase the user puts bad input.
    n=0 
#now Python is going to run the loop for the n times since those were the business transactions
#we use a for loop since we know the number of times for it to run
for i in range(n):
    print("Transcation", i + 1)
    name= input("Please Enter the Name of the student: ")
    try :
        year=int(input("What is their year of study?(1 to 4) "))
    except ValueError:
        print("Please enter a valid year of study")
        year = 0
    type_of_book = input("Have they borrowed a Textbook,Novel or Reference? ")
    #now we check conditions
    #we use or since only one condition has to be met
    if year <1 or year >4:
        print("Rejected! This is an invalid study year!")
    elif max_no_of_days(type_of_book) == 0:
        print("Rejected! That type of book doesn't exsist here!")
    elif type_of_book=="Reference" and which_year_can_borrow_reference(year)== False:
        print("Rejected! Reference books can only be borrowed by Year 3 and Year 4.")
    else:
        print(name,"can borrow a",type_of_book,"for",max_no_of_days(type_of_book),"days!" )
        successful = successful +1 
        if type_of_book == "Textbook":
           textbooks = textbooks + 1
        elif type_of_book == "Novel":
           novels = novels + 1
        else :
           references = references +1 
print("Successful number of borrowings:",successful)
print("Number of Textbooks borrowed:",textbooks)
print("Number of Novels borrowed:",novels)
print("Number of References Borrowed:",references)
        
        
        
        
    
    
     
    
    