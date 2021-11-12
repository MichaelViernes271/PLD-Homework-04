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
    name, age, address = "", "", ""
    name = input("Your name: ")
    age = input("Your age: ")
    address = input("Your address: ")
    return name, age, address # end getInfo()

def printInfo(user_name, user_age, user_address):
    print(f"Hi, my name is {user_name}. I am {user_age} years old and I live in {user_address}.")

def main(): # define main program
    """
    Creating array. # THE FOLLOWING CODE WILL NOT BE USED!
    #info = []
        # THE FOLLOWING CODE WILL NOT BE USED!
        #info.append(getName())
        #info.append(getAge())
        #info.append(getAddress())
    """
    
    m_name ,m_age ,m_address = getInfo()
    printInfo(m_name, m_age, m_address)

while True:
    quit = "None"
    main() # call main program
    quit = input("Press Q to quit: ")
    if str(quit).upper() == "Q": # Experimented on str's upper func.
    
        # Experimented on multi line prints.
        
        print(
        """Thank you for your participation."""
        )
        break

