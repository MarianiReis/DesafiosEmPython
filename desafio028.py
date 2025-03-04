


import math

def fatorial(n):
    if n == 0 or n == 1:
      return 1
    else:
        return n * fatorial(n-1)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def mdc(a,b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b) 



def mmc(a, b):

    return abs(a * b) // math.gcd(a,b)

