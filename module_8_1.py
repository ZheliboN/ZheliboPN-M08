def add_everything_up(a, b):
    summa = 0
    try:
        summa = a + b
    except TypeError:
        summa = str(a)+str(b)
    else:
        summa = round(a + b, 3)
    finally:
        return summa


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
