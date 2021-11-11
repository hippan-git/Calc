# 48:57 - '0:9'
# 46 - '.'
# 44 - ','

import myFunc
def filter(ls: list):
    """очистка листа от постороннего мусора"""
    digits = tuple(chr(x) for x in range(42, 58) if x != 44)  # Шаблон цифр и знаков
    garbage_list = []
    for it_s in ls:
        if not it_s in digits:
            garbage_list.append(it_s)
    for gar in garbage_list:
        ls.remove(gar)


def calculate(calc_list: list, sign: str):
    res = None  # FIXIT
    x, y = float(calc_list[0]), float(calc_list[1])
    if sign == '*':
        res = x * y
    elif sign == '/':
        res = x / y
    elif sign == '+':
        res = x + y
    elif sign == '-':
        res = x - y
    return str(res)


def separate(ls: list, sign: str) -> list:
    """
    отделяет одно из четырех действий (*, /, -, +)\n
    возвращает список с результатом вместо действия
    Прим.\n ls = ['3', '8', '7', '+', '6','2','5', '*', '2','2','5', '-', '8', '5', '*', '4', '8', '3']\n
    sign = '*'\n
    вернет ['3', '8', '7', '+', '140625', '-', '8', '5', '*', '4', '8', '3']
    """
    start_r, end_r = None, None
    for it in range(ls.index(sign) - 1, -1, -1):
        if not it:
            start_r = 0
        elif not ls[it].isdigit():
            if '.' in ls[it]:
                continue
            start_r = it + 1
            break

    for it in range(ls.index(sign) + 1, len(ls)):
        if it == len(ls) - 1:
            end_r = len(ls)
        elif not ls[it].isdigit():
            if '.' in ls[it]:
                continue
            end_r = it
            break

    s = ''.join(ls[start_r:end_r])
    del ls[start_r:end_r]
    ls.insert(start_r, calculate(s.split(sign), sign))
    return ls


def find_first_sign(ls: list) -> str:
    pattern_sign_first = '*', '/'
    pattern_sign_second = '+', '-'
    for it in ls:
        if it in pattern_sign_first:
            return it
    for it in ls:
        if it in pattern_sign_second:
            return it
    pass


s = '387 + 625 * 225 - 85 * 484 / 2'
ls = list(s)
del s
filter(ls)
isNotCalc = True
while isNotCalc:
    isNotCalc = False
    f_sign = find_first_sign(ls)
    if f_sign == '*':
        ls = separate(ls, '*')
        isNotCalc = True
        continue
    elif f_sign == '/':
        ls = separate(ls, '/')
        isNotCalc = True
        continue
    elif f_sign == '+':
        ls = separate(ls, '+')
        isNotCalc = True
        continue
    elif f_sign == '-':
        ls = separate(ls, '-')
        isNotCalc = True
print(ls)
print(387 + 625 * 225 - 85 * 484 / 2)
