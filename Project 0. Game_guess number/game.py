"""Game: guess number"""

import numpy as np

number = np.random.randint(1, 101) # specify number

# number of attempts
count = 0

while True:
    count+=1
    predict_number = int(input("Guess number from 1 to 100: "))
    
    if predict_number > number:
        print("Number should be less!")

    elif predict_number < number:
        print("Number should be greater!")
    
    else:
        print(f"You guessed correct number! This number = {number}, per {count} attempts")
        break #end game exit cycle