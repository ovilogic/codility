#! python3
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        print(a)
        c = a + b
        a, b = b, c


fibonacci(45)
