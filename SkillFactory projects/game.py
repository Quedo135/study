"""Guess a number"""
import numpy as np

def random_predict(number: int = 1) -> int:
    """Trying to catch the number

    Args:
            n (int, optional): input number. Defaults to 1.
    Returns:
            int: number of tries
    """

    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)

def score_game(predict_method, tries_num:int = 10) -> int:
    """Calculation of method work (mean from 1000 numbers)

    Args:
        predict_method (_type_): method

    Returns:
        int: mean number of tries
    """
    count_arr = []
    np.random.seed(1)
    for i in range(tries_num):
        count_arr.append(predict_method(np.random.randint(1, 101)))
        
    return sum(count_arr) / tries_num
