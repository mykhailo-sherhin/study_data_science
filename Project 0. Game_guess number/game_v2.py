"""Game: guess number
Computer itself guesses and looks for number
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Randomly specify number

    Args:
        number (int, optional): Specified number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # guessed number
        if number == predict_number:
            break  # exit cycle if number was found
    return count


def score_game(random_predict) -> int:
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
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm finds number in average per:{score} attempts")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
