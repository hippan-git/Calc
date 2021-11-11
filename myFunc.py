def fib(n):
    if n < 2:
        return n
    else:
        r = fib(n-1) + fib(n-2)
        return r


def inputDig(pre='') -> int or float:
    """Возвращает int при отсутствии точки
    или float при ее наличии. Если больше одной точки
    потребует ввод заново"""
    while True:
        a = input(pre)
        arr = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.' in a
        if not False in arr and a.count('.') == 1:
            """вхождение при присутствии точки
            следовательно на выходе float"""
            return float(a)
        elif a.isdigit():
            return int(a)

