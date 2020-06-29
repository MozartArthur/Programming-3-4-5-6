# реализовать генератор чисел ряда Фибоначчи. Генератор требуется создать двумя вариантами: с помощью генератора списков, с помощью функции, внутри которой yield.
def recursive_fibo(n):
    if n>=2:
        return recursive_fibo(n-1)+recursive_fibo(n-2)
    else:
        return 1

def fibo_list(n):
    return [ recursive_fibo(i) for i in range(0,n) ]

def fibo_yield(n):
    for i in range(0,n):
        yield recursive_fibo(i)

print(list(fibo_yield(10)))
