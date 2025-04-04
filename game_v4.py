import numpy as np

def binary_predict(number: int = 1) -> int:
    """Оптимизированный алгоритм угадывания числа методом бинарного поиска.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    low, high = 1, 100  # границы поиска
    count = 0  # счётчик попыток

    while True:
        count += 1
        predict = (low + high) // 2  # предположение — середина диапазона

        if predict == number:
            return count
        elif predict < number:
            low = predict + 1  # сдвигаем нижнюю границу
        else:
            high = predict - 1  # сдвигаем верхнюю границу

def score_game(predict_function) -> int:
    """Вычисляет среднее количество попыток для угадывания числа за 1000 итераций.

    Args:
        predict_function (function): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)  # генерируем 1000 случайных чисел

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls))  # среднее количество попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    # Запуск
    score_game(binary_predict)
