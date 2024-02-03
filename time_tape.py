#! python3
'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and
A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of:
 |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def solution_nonefficient(A):
    results = []
    for P in range(1, len(A)):

        left = A[:P]

        right = A[P:]

        sum_left = 0
        sum_right = 0
        i = 0
        while i < len(left):
            sum_left += left[i]
            i += 1
        i = 0
        while i < len(right):
            sum_right += right[i]
            i += 1
        diff = abs(sum_left - sum_right)
        results.append(diff)
    for i in range(len(results) - 1):
        if results[i] < results[i + 1]:
            result = results[i]
        else:
            result = results[i + 1]
    return result


A = [i for i in range(5)]
A[0] = 3
A[1] = 1
A[2] = 2
A[3] = 4
A[4] = 3

B = [-1000, 1000]


def solution(A):
    sum_ = 0
    i = 0
    sums_left = []
    # You need the absolute sum as it is the biggest number to compare all the possible differences.
    sum_abs = 0
    # The important thing is to have for-loops or while-loops side by side rather than one inside the other. As long as
    # you do that, it's still O(n) rather than O(n**2).
    while i < len(A):
        sum_ += A[i]
        if i < len(A) -1:
            sums_left.append(sum_)
        sum_abs += abs(A[i])
        i += 1
    result = sum_abs
    for i in range(1, len(A)):
        right = sum_ - sums_left[i - 1]
        left = sums_left[i - 1]
        diff = abs(left - right)
        if diff < result:
            result = diff
    return result


print(solution(A))




