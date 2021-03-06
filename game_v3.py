"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    number = np.random.randint(1,101)  # задаем случайное число
    predict = 50  # предполагаем, что переменная равна "50"
    count = 1  # задаем счётчик операций
    if predict < number: # проверяем соотвествует ли переменная условию
        predict += 25 
        count += 1
        if predict < number:
            predict += 12
            count += 1
            if predict < number:
                predict += 8
                count += 1
            else:
                predict -= 6
                count += 1
        elif predict > number:
            predict -= 12
            count += 1
            if predict < number:
                predict += 8
                count += 1
            else:
                predict -= 6
                count += 1
    elif predict > number:
        predict -= 25
        count += 1
        if predict < number:
            predict += 12
            count += 1
            if predict < number:
                predict += 8
                count += 1
            else:
                predict -= 6
                count += 1
        elif predict > number:
            predict -= 12
            count += 1
            if predict < number:
                predict += 8
                count += 1
            else:
                predict -= 6
                count += 1
    while predict < number:
        predict += 1
        count += 1
    while predict > number:
        predict -= 1
        count += 1
    return count  # показываем счётчик операций


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
