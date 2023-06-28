import datetime

users = [
    {'name': 'Bill', 'birthday': datetime.date(2023, 7, 2)},
    {'name': 'Jill', 'birthday': datetime.date(2023, 7, 3)},
    {'name': 'Kim', 'birthday': datetime.date(2023, 7, 4)},
    {'name': 'Jan', 'birthday': datetime.date(2023, 7, 7)},
    {'name': 'Alex', 'birthday': datetime.date(2023, 7, 9)},
    {'name': 'Ben', 'birthday': datetime.date(2023, 7, 12)}

]

def get_birthdays_per_week(users):
    current_date = datetime.datetime.now().date()
    current_weekday = current_date.weekday()
    next_week_start = current_date + datetime.timedelta(days=(7 - current_weekday))
    next_week_end = next_week_start + datetime.timedelta(days=6)

    birthdays = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 
                 'Saturday': [], 'Sunday': []}

    for user in users:
        birthday = user['birthday']
        if next_week_start <= birthday <= next_week_end:
            birthday_weekday = birthday.weekday()

            if birthday_weekday >= 5:
                birthdays['Monday'].append(user['name'])
            else:
                birthday_name = birthday.strftime('%A')
                birthdays[birthday_name].append(user['name'])

    for weekday, user_list in birthdays.items():
        if user_list:
            print(f"{weekday}: {', '.join(user_list)}")

get_birthdays_per_week(users)