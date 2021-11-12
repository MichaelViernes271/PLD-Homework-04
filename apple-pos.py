#apple pos
"""
Programming Logic and Design: Homework 03
Author: Viernes, Michael
Submitted to: Mr. Madrigalejos
"""

print("----------------------------------------")
print("\t\tApples")
print("----------------------------------------")
    
def calcApples(): # Calculates apples.
    savings = float(input("Amount of your money: "))
    apple = float(input("How much apple will you buy: "))
    return savings, apple
    # End calcApples().

def calcChange(savings, apple): # Calculates savings change.
    money_change = savings - apple
    
    if money_change < 0:
        print("You had bought too many apples!")
        calcApples()
    else:
        print(f"You can buy {int(apple)} apples and" + 
        f" your change is {str(float(money_change))} pesos.")
    # End calcChange().
    
    # testing pass keyword 
    # NOVEMBER 12, 2021 EDIT: The purpose is common for loops.

# main function call
def main():
    while True: # Loop statement copied from name-intro.py.
        quit = "None" # Initializes quit variable.
        m_savings, m_apple = calcApples()
        calcChange(m_savings, m_apple)
        quit = input("(Q to quit): ")
        if str(quit).upper() == "Q": # Experimented on str's upper func.
        
            # Experimented on multi line prints.
            print(
            """\nThank you for your participation.\n"""
            )
            
            break

    
main() # Start calling main().