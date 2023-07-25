'''
Функція get_birthdays_per_week отримує на вхід список users і виводить у консоль 
(за допомогою print) список дюдей, яких потрібно привітати по днях тижня.
'''

from datetime import datetime, timedelta

def get_birthdays_per_week(users: list):
    current_datetime = datetime.now()
    next_week = current_datetime + timedelta(weeks=1)
    birthday_dictionary = {}
    for user in users:
        birthday = user['birthday']
        birthday_in_this_year = birthday.replace(year=current_datetime.year)
        name = user['name']
        
        # Перевіремо, чи є днюхи протягом тижня
        if current_datetime <= birthday_in_this_year < next_week:
            
            # Якщо днюха на вихідних, вітаємо в понеділок
            if birthday_in_this_year.weekday() in [5, 6]:  # 5 - субота, 6 - неділя
                days_until_monday = (7 - birthday_in_this_year.weekday()) % 7
                greeting_date = birthday_in_this_year + timedelta(days=days_until_monday)
                birthday_dictionary.setdefault(greeting_date.strftime('%A'), []).append(name)
                
            else:
                birthday_dictionary.setdefault(birthday_in_this_year.strftime('%A'), []).append(name)
    # Виводимо в консоль отриманий список іменинників            
    for key, value in birthday_dictionary.items():
        print(f'{key}: {", ".join(value)}')    

"""
# Тестовий приклад для обкатки:
users = [
    {'name': 'Пупкін', 'birthday': datetime(2008, 7, 26)},
    {'name': 'Шнурапет', 'birthday': datetime(2006, 7, 27)},
    {'name': 'Абебі', 'birthday': datetime(1983, 7, 25)},
    {'name': 'Дракула', 'birthday': datetime(1367, 7, 30)},
    {'name': 'Хрюкіна', 'birthday': datetime(2000, 7, 24)},
    {'name': 'Мозгоедова', 'birthday': datetime(1945, 3, 12)},
    {'name': 'Бібік', 'birthday': datetime(1985, 6, 15)},
    {'name': 'Горець', 'birthday': datetime(1702, 7, 30)},
]

get_birthdays_per_week(users)
"""