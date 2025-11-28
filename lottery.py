import random

def get_numbers_ticket(min_value, max_value, quantity):
    """
    Функція повертає випадковий набір чисел в межах заданих параметрів, 
    причому всі випадкові числа в наборі будуть унікальні.

    Параметри:
    min_value - мінімальне значення діапазону, ціле число, що становить щонайменше 1
    max_value - максимальне значення діапазону, ціле число, що становить щонайбільше 1000
    quantity - кількість унікальних чисел, які потрібно згенерувати

    """
    set_of_nums=set() #використовуємо set, щоб уникнути дублікатів 
    if min_value>=1 and max_value<=1000 and 1 <= quantity <= (max_value - min_value + 1): #перевіряємо значення крайніх чисел діапазону та переконуємось, 
        #що кількість унікальних чисел quantity не перевищує кількість чисел у діапазоні
        
        while (len(set_of_nums))<quantity: #цикл буде виконуватись, поки кількість num y set_of_num не буде дорівнювати quantity
            num=random.randint(min_value, max_value)
            set_of_nums.add(num)
        ticket=sorted(set_of_nums)
        return ticket


    else:
        return []
    
while True:
    min_value=int(input('Введіть мінімальне значення: '))
    max_value=int(input('Введіть максимальне значення: '))
    quantity=int(input('Введіть кількість унікальних чисел, які потрібно згенерувати: '))
    try:
        get_numbers_ticket(min_value, max_value, quantity) #викликаємо функцію get_numbers_ticket
        print (f'Виграшний квиток: {ticket}')
        break #виходимо з циклу, якщо все введено правильно
    except ValueError:
        print (f'Невірні параметри, спробуйте ще раз') #обробляємо помилку, якщо параметри неправильні, та повторно запускаємо функцію
        

