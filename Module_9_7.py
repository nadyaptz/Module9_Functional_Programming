def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        k = 0
        for i in range(2, result // 2 + 1):
            if (result % i == 0):
                k = k + 1
        if (k <= 0):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper
@is_prime
def sum_three(one, two, three):
    return one+two+three

print(sum_three(2, 3, 6))