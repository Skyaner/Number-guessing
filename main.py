import random


print("This is a simple number guessing game.\n")
print("Range: (min,max)\n")


while TRUE:
    # input check
    try:
        min = int(input("Minimum: "))
    except:
        print("This is not a valid input!!! \n")
        continue
                
    try:
        max = int(input("Maximum: "))     
    except:
        print("This is not a valid input!!! \n")      
        continue
    
    # range
    if max > min and min >= 0:
        Number  = random.randint(min,max)
        break
    elif min < 0:
        print("Your minimum should start at 0 or higher \n")
       
    else:
        print("Your minimum is greater than or equal to your maximum \n")       
        continue
    
print(Number)

x = -1
c = 0

while x  != Number:
    # range
    print(f"The number is between [{min},{max}] \n")
    
    # input check
    try:
        x = int(input("Your guess: "))
    except:
        print("Please enter an integer \n")
        continue 
    
    # counter
    c += 1
    
    # game logic
    if x > max or x < min:
        print("Your guess is outside of your range \n")
     
    elif x - 5 > Number :
        print("You guessed to high \n")
        
    elif x > Number:
        print("You guessed a little to high \n")
       
    elif x + 5 < Number:
        print("You guessed to low \n")
         
    elif x < Number:
        print("You guessed a little to low \n")
        
    else:
        print("Congratulation, you did it \n")
        print(f"It took you {c} tries")
         