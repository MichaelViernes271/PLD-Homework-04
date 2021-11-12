#apple and orange pos
"""
Topic: Programming Logic and Design
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
"""

def printTotal(sum): # Prints total.
    print(f"The total amount of fruits is {sum}.")
    # end printTotal()

def calcFruits(apples, orange): # Calculates sum of fruits.
    sum = (apples * 20) + (orange * 25)
    print("$20 * Apples = " + str(apples * 20))
    print("$25 * Orange = " + str(orange * 25))
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

payFruits()# Call payFruits