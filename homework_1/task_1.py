from datetime import datetime


def get_days_from_today(date: str) ->int:
    """
    Функція розраховує кількість днів між заданою датою та поточною датою.
    
    Параметри:
    date - String, що позначає дату в форматі YY-MM-DD.

    Повертає:
    num_of_days - int, що покахує різницю між поточною та заданою датою. Якщо date в майбутньому, повертає від'ємне число.
    
    ValueError, якщо рядок date не відповідає формату 'YYYY-MM-DD'.
    """
    date_given=datetime.strptime(date, '%Y-%m-%d').date() #переводимо date із формату String в об'єкт datetime у форматі '%Y-%m-%d'
    date_current=datetime.today().date() #визначаємо поточну дату
    num_of_days=(date_current-date_given).days #вираховуємо різницю між поточною та заданою датою
    return num_of_days


    
while True:
    date=input(str('Введіть дату: ')) #користувач вводить дату
    
    try:
        get_days_from_today(date) #викликаємо функцію days_from_today 
        print(get_days_from_today(date))
        break #виходимо з циклу, якщо дата введена правильно
    except ValueError:
        print (f'Невірно введена дата. Спробуйте ще раз.') #обробляємо помилку, якщо дата вказана в неправильному форматі, та повторно запускаємо функцію
        

