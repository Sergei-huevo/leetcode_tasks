def factorial_by_cycle_while(n):
    if n == 0:
        return 0
    i = 0
    fac = 1
    while i != n:
        fac *= i + 1
        i += 1
    return fac


def factorial_by_cycle_for(n):
    if n == 0:
        return 0
    fac = 1
    for i in range(1, 11, 1):  # цикл да 11, 11 не входит в прербор
        fac *= i
    return fac


# я все - равно не понимаю, как это работает (18.05.2021)
def factorial_by_recursion(n):
    if n == 1:
        return n
    else:
        return n * factorial_by_recursion(n - 1)


def any_recursion(n):
    if n == 1:
        a = 1 + 1 + 1 + 1
        print(f'Stop! {a} раза уже сказал')
    else:
        print('Hello')
        any_recursion(n - 1)


def fibonacci_by_recursion(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci_by_recursion(n - 1) + fibonacci_by_recursion(n - 2)



