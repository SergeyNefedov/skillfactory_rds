import numpy as np

def game_core_v3(number):
    count = 1
   # Воспользуемся алгоритмом половинного деления (дихотомии)
   # Зададим нижнюю и верхнюю границу интервала, в котором ищем число
   # Очередное предсказание будет равняться середине интервала, который будет сокращаться в 2 раза с каждым шагом
    predict_low = 0
    predict_up = 100
    predict = 50
   # print('Ищем в диапазоне от {} до {}'.format(predict_low,predict_up))
    while number != predict:
        if number > predict:
            count += 1
            predict_low = predict
            predict = int(round((predict_up+predict_low)/2))
           # print('Ищем в диапазоне от {} до {}'.format(predict_low,predict_up))
        elif number < predict:
            count += 1
            predict_up = predict
            predict = int(round((predict_up+predict_low)/2))
           # print('Ищем в диапазоне от {} до {}'.format(predict_low,predict_up))
    if number!= 50:
        count += 1
    return count
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
        
# Проверяем
score_game(game_core_v3)