#шуточное приложение "магический шар"

import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как твоё имя: ')
print('Привет', name)
while True:
    question = input('Задай свой вопрос: ')
    print(random.choice(answers))
    answer = input('Может ты хочешь ещё о чем то спросить?: ')
    if answer == 'yes':
        continue
    else:
        print('Был рад ответить на твои вопросы, возвращайся!')
        break