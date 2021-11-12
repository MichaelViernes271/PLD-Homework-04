#name introduction
"""
Topic: Programming Logic and Design
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
"""

print("--------------------")
print("\tIntroduction")
print("--------------------")

"""
# Getter functions (NOT USED FOR THE MOMENT FOR HOMEWORK 04).
def getName():
    name = input("Your name: ")
    return name
    
def getAge():
    age = input("Your age: ")
    return age
    
def getAddress():
    address = input("Your address: ")
    return address
"""

def getInfo(): # gets name, age, address
    # declare info local variables
    name, age, address = None
    while name and age and address == None:
        name = input("Your name: ")
        age = input("Your age: ")
        address = input("Your address: ")
    return name, age, address # end getInfo()

def printInfo(userInfo):
    print(f"Hi, my name is {userInfo[0]}. I am {userInfo[1]} years old and I live in {userInfo[2]}.")

# define main program
def main():
    # Creating array. # THE FOLLOWING CODE WILL NOT BE USED!
    #info = []
    try:
        # THE FOLLOWING CODE WILL NOT BE USED!
        #info.append(getName())
        #info.append(getAge())
        #info.append(getAddress())   
        
    except Error:
        print("Please put a proper input.")
    printInfo(info)

while True:
    quit = "None"
    main() # call main program
    quit = input("Press Q to quit: ")
    if (quit == "q".upper())
        break

