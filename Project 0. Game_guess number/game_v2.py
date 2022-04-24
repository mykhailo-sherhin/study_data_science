"""Game: guess number
Computer itself guesses and looks for number
"""

import numpy as np


def predict_number(number: int = 1) -> int:
    """Randomly specify number

    Args:
        number (int, optional): Specified number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0
    predict_number = 50
    step_number = 50

    while True:
        count += 1
        if step_number == 101:
            step_number = 2
        else:
            step_number //= 2
    
        if predict_number > number:
            predict_number -= step_number
        
        elif predict_number < number:
            predict_number += step_number
        
        else:
            break  # exit cycle if number was found
        
        if step_number == 1:
            step_number = 101
            
    return count


def score_game(predict_number) -> int:
    """Average number of attempts of finding number for 1000 tries

    Args:
        random_predict ([type]): predict function

    Returns:
        int: average number of attempts
    """
    count_ls = []
    #np.random.seed(1)  # fix seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # specified list of numbers

    for number in random_array:
        count_ls.append(predict_number(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm finds number in average per:{score} attempts")
    return score


score_game(predict_number)