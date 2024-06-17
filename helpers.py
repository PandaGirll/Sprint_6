import random

from datetime import date, timedelta


# Генерируем словарь для заполнения формы заказа
def generate_order_info():
    metro_stations = ["Красные Ворота", "Чистые пруды", "Лубянка",
                      "Кузнецкий Мост", "Китай-город", "Третьяковская",
                      "Новокузнецкая", "Боровицкая", "Александровский сад"]
    colors = ['black', 'grey']
    rental_durations = ['сутки', 'двое суток', 'трое суток', 'четверо суток',
                        'пятеро суток', 'шестеро суток', 'семеро суток']

    return {
        'name': random.choice(['Саша', 'Маша', 'Петя', 'Вася']),
        'surname': random.choice(['Петров', 'Огурцов', 'Сидоров', 'Тестеров']),
        'address': random.choice(['Москва, Петровка', 'Питер 228',
                                  'Город, улица, дом', 'Сюда и туда']),
        'metro': random.choice(metro_stations),
        'phone': random.randint(10000000000, 99999999999),
        'date': (date.today() + timedelta(
            days=random.randint(1, 7))).strftime('%d.%m.%Y'),
        'duration': random.choice(rental_durations),
        'color': random.choice(colors),
        'comment': random.choice(['', 'позвонить за час', 'оставить у двери',
                                  'домофон не работает'])
    }
