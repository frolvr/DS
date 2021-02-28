import numpy as np

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    a = 1
    b = 100
    predict = np.random.randint(a,b)
    #print("Загадано число от 1 до 100")
    #print("Это число",predict)
    count = 1
    number = b // 2
    while number != predict:
        count = count + 1
        if number > predict:
            b = number
        elif number < predict: 
            a = number
        number = (b - a) // 2 + a
        
    return count # выход из цикла, если угадали

#game_core_v2(number)
def score_game(game_core_v2):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(a,b, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v2(number))
        score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    
    return score

score_game(game_core_v2)
