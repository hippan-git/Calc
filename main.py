M = {0: 0, 1: 1}


def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a


r = [0]
a = input('Введите число ')
f = fib(int(a))
print(f'число фибоначи от {a}: {f}')
