#! python3
''' An array A consisting of N different integers is given.
 The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.
N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].'''
import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


B = [x for x in range(1, 9)]

for x in range(356):
    i = random.randrange(8)
    B[i], B[2] = B[2], B[i]
A = B[:7]
print(B)
print(A)


def solution(A):
    N = len(A)
    sum = (N + 1) * N // 2
    sum_real = 0
    for i in A:
        sum_real += i
    print(sum_real, sum)
    difference = sum_real - sum
    odd_one = N + 1 - difference
    return odd_one


print(solution(A))