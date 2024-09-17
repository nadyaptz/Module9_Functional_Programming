def apply_all_func(int_list, *functions):
    result = {}
    try:
        for func in functions:
            result[func.__name__] = func(int_list)
    except TypeError:
        print('В функцию передан неверный формат данных - нужен список из чисел')
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))