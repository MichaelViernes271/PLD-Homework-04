#apple and orange pos
"""
Topic: Programming Logic and Design
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
"""

def printTotal(sum): # Prints total.
    print("The total amount of fruits is {0}.".format(sum)) # Trying new format
    # end printTotal()

def calcFruits(apples, orange): # Calculates sum of fruits.
    sum = (apples * 20) + (orange * 25)
    print(f"$20 x {apples} Apples = " + str(apples * 20))
    print(f"$25 x {orange} Orange = " + str(orange * 25))
    return sum
    # end calcFruits()

def payFruits(): # Customer pays.
    print("-------------------------------")
    print("\tApple and orange")
    print("-------------------------------")
    
    customer = input("Hello, Mr/Ms: ")
    print(f"Hello {customer}\n")
    
    try:
        apples = int(input(f"How many apples will you buy: "))
        orange = int(input(f"How many orange will you buy: "))
    except Exception:
        print("Please input a number. \n")
            
    sum = calcFruits(apples, orange)
    printTotal(sum)
    # end payFruits()


while True: # Loop copied from name-intro.py.
    quit = "None"
    payFruits()# Call payFruits
    quit = input("Press Q to quit: ")
    if str(quit).upper() == "Q": # Experimented on str's upper func.
    
        # Experimented on multi line prints.
        print(
        """Thank you for your participation.\n"""
        )
        
        break