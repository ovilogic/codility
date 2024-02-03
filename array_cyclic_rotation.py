#! python3
''' An array A consisting of N integers is given. Rotation of the array means that each element is shifted
 right by one index, and the last element of the array is moved to the first place. For example, the rotation of
 array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
  (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].'''
import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

A = [3, 8, 9, 7, 6]
K = 7


def solution(A, K):
    if len(A) == 0:
        return A
    while K > len(A):
        K -= len(A)
    rump = A[-K:]
    for a in range(len(rump)):
        x = A.pop()
        A.insert(0, x)
    print(A)


# for i in range(10):
#     random_array = [random.randrange(-1000, 1000) for i in range(random.randrange(100))]
#     random_k = random.randrange(100)
#     solution(random_array, random_k)

solution(A, K)