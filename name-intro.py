#name introduction
"""
Topic: Programming Logic and Design
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
"""

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

def getInfo(): # gets name, age, address.
    # Declares info local variables.
    name, age, address = "", "", ""
    name = input("Your name: ")
    age = input("Your age: ")
    address = input("Your address: ")
    return name, age, address # end getInfo()

def printInfo(user_name, user_age, user_address):
    print(f"\n\nHi, my name is {user_name}. I am {user_age} years old and I live in {user_address}.\n")

"""
def decorator(decorFunc): # This will be added at some point.
    def consoleDecorator():
        return
    return consoleDecorator
"""
    
def main(): # REDEFINED main program.
    """
    Creating array. # THE FOLLOWING CODE WILL NOT BE USED!
    #info = []
        # THE FOLLOWING CODE WILL NOT BE USED!
        #info.append(getName())
        #info.append(getAge())
        #info.append(getAddress())
    """
    
    
    print("\n--------------------")
    print("\tIntroduction")
    print("--------------------")
    print("\tRequesting Personal Information: \n\n")

    m_name ,m_age ,m_address = getInfo()
    printInfo(m_name, m_age, m_address)

while True:
    quit = "None"
    main() # Calls main program.
    quit = input("Press Q to quit: ")
    if str(quit).upper() == "Q": # Experimented on str's upper func.
    
        # Experimented on multi line prints.
        print(
        """Thank you for your participation.\n"""
        )
        
        break

