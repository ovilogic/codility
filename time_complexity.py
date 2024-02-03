#! python3
''' You are given an integer n. Count the total of 1 + 2 + . . . + n '''
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def solution(n):
    if n % 2 == 0:
        result = (n + 1) * (n / 2)
    else:
        result = n * (n - 1) / 2 + n
    return result


# Time complexity is O(1)
print(int(solution(5)))


def model_solution(n):
    # Odd number times even number always returns an even number.
    result = n * (n + 1) // 2
    return result


print(model_solution(5))