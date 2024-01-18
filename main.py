import random


i = 1

while i == 1:
    # input check
    try:
        min = int(input("Minimum: "))
    except:
        print("This is not a valid input!!!")
        continue
                
    try:
        max = int(input("Maximum: "))     
    except:
        print("This is not a valid input!!!")
        continue
    
    # range
    if max > min:
        Number  = random.randint(min,max)
        break
    else:
        print("Your minimum is greater than or equal to your maximum")
        continue
    
print(Number)

x = -1

while x  != Number:
    # range
    print(f"The number is between [{min},{max}]")
    
    # input check
    try:
        x = int(input("Your guess: "))
    except:
        print("Please enter an integer")
        continue 
    
    # game logic
    if x > max or x < min:
        print("Your guess is outside of your range") 
    elif x - 5 > Number :
        print("You guessed to high")
    elif x > Number:
        print("You guessed a little to high")
    elif x + 5 < Number:
        print("You guessed to low")
    elif x < Number:
        print("You guessed a little to low")
    else:
        print("Congratulation, you did it")