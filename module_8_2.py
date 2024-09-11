def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {num}')
    a = (result, incorrect_data)
    return a


def calculate_average(numbers):
    summa = 0
    try:
        summa = personal_sum(numbers)
        summa = summa[0]/(len(numbers)-summa[1])
    except TypeError:
        print('В numbers записан некорректный тип данных')
        summa = None
    except ZeroDivisionError:
        summa = 0
    finally:
        return summa


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
