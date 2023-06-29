import datetime

def get_birthdays_per_week(users):
    current_date = datetime.datetime.now().date()
    current_weekday = current_date.weekday()
    next_week_start = current_date + datetime.timedelta(days=(5 - current_weekday))
    next_week_end = next_week_start + datetime.timedelta(days=6)

    birthdays = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 
                 'Saturday': [], 'Sunday': []}

    for user in users:
        birthday = user['birthday'].date()

        if next_week_start <= birthday <= next_week_end:
            birthday_weekday = birthday.weekday()

            if birthday_weekday >= 5:
                birthdays['Monday'].append(user['name'])
            else:
                birthday_name = datetime.date.strftime(birthday, '%A')
                birthdays[birthday_name].append(user['name'])

    for weekday, user_list in birthdays.items():
        if user_list:
            print(f"{weekday}: {', '.join(user_list)}")

users = [
    {'name': 'Bill', 'birthday': datetime.datetime(2023, 7, 1)},
    {'name': 'Jill', 'birthday': datetime.datetime(2023, 7, 2)},
    {'name': 'Kim', 'birthday': datetime.datetime(2023, 7, 4)},
    {'name': 'Jan', 'birthday': datetime.datetime(2023, 7, 7)},
    {'name': 'Alex', 'birthday': datetime.datetime(2023, 7, 8)},
    {'name': 'Ben', 'birthday': datetime.datetime(2023, 7, 9)}
]
# Якщо я правильно зозумів умову завдання, то в понеділок попадають тільки вихідні поточного тиждня,
# вихідні наступного тиждня потрапляють на наступний понеділок, при запуску коду на наступному тижні.
get_birthdays_per_week(users)
