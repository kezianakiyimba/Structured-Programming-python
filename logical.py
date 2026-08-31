print (True or False)
print( True and False)
#defining the variables
x=10
y=5
#the following are the relational operators
print(x==10)
print(x!=10)
print(y==5)
print(y!=5)
print(x>=y)
print(x<=y)
#the above are the relational operators
test1=int(input("Enter score in test1:"))
test2=int(input("Enter score in test2:"))
test3=int(input("Enter score in test3:"))
average= (test1+test2+test3)/3#this calculates the average score of the three tests
print(f"The average score is {average}")#this is the average score of the three tests
#the code below checks if the average score is greater than or equal to 85, and prints a message accordingly
if average>=85:
    print("You have passed the test")
else:
    print("You have not passed the test")
x=int(input("Enter a number:"))
#the code below checks if the number entered is positive, and prints a message accordingly
#and if it is not positive, it prints a different message
if x>0:
    print(f"The number {x} is positive")
    print(f"Positive numbers are greater than zero")
else:
    print(f"The number {x} is not positive")
print("Thanks for your time!")
x=int(input("Enter a number:"))
if x%2==0:
    print(f"The number {x} is even.")
else:
    print(f"The number {x} is odd.")
x=int(input("Enter a number:"))
if x<0 and x>100:
    print(f"The number {x} is out of range.")   