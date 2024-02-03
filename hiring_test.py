#! python3
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def sol(nos):
    nos.sort()
    max = nos[-1]
    if max % 2 == 0:
        max2 = [i for i in nos[:-1] if i % 2 != 0][-1]
        print(max2)
    # else:
        # max2 = [i for i in nos[:-1]] if i % 2 == 0][-1]


x = [20, 10, 7, 5]
sol(x)
