
def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        is_prime = True
        for i in range(2, res//2 + 1):
            if res % i == 0:
                is_prime = False
        if is_prime:
            print(' Простое')
        else:
            print('Составное')
        return res
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a+b+c




result = sum_three(2, 3, 6)
print(result)
result = sum_three(5, 7, 20)
print(result)