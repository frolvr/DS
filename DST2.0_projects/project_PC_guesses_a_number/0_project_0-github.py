#
# Компьютер загадывает число от 1 до 100. 
# За основу взят медом деления отрезка попалам. 
# Зная длину отрезка, устанавливаем его середину. 
# Затем каждую итерацию уменьшаем устанавливаемое число в два раза,
# округляя до целого. 
# Наш отрезок = 100. Полученные числа = 50, 25, 12, 6, 3, 1. 
# Основываясь на подсказке - "число больше" или "число меньше" загаданного, 
# каждую итерацию мы уменьшаем или увеличиваем искомое число
# на полученное число в порядке убывания. 
# В результате мы получаем максимум 7 итераций.
# 

import numpy as np


def game_core(number):
    """Функция принимает загаданное число и возвращает число попыток."""
    
    min = 1
    max = 100
    predict = np.random.randint(min,max) # компьютер загадал число
    count = 1
    number = max//2
    while number != predict:
        count += 1
        if number > predict:
            max = number
        elif number < predict:
            min = number
        number = (max-min)//2 + min # применяем формулу метода

    return count # выход из цикла, если угадали

    def score_game(game_core):
        """Запускаем игру 1000 раз,
        чтобы узнать среднее количество раз,     
        необходимое игре для нахождения загаданного числа.
    
        """
        global min, max
        count_list = []
        np.random.seed(1)  # фиксируем SEED для воспроизведения эксперимента
        random_array = np.random.randint(min,max, size=(1000))
        for number in random_array:
            count_list.append(game_core(number))
            score = int(np.mean(count_list)) # подсчет среднего значения попыток
        print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

        return score

score_game(game_core)
