#! python3
'''
An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N.
The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
'''
import logging
import math

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def solution(N):
    # Smallest numbers will be the ones on either side sqrt(N). That is, the smallest ones, closest ones to sqrt(N).
    # This was gleaned by looking at the example case provided.
    '''
    Mathematical proof:
    1. We note all potential scenarios can be sorted according to the following pattern, starting with case a, where
    one side is equal to the area and the other side equal to 1.
    N = area
    N = A * B
    a. A = N, B = 1
    b. A = N / 2, B = 2 --> Hypothesis says "The sides of this rectangle should be only integers."
    So next B can only be 1,
    and next one 2, then 3 etc.
    c. A = N / 3, B = 3

    2. Case a gives Perimeter (P) = (N+1)2 = 2N + 2. Case b, (N/2 + 2)2 = N + 4, c, (N/3 + 3)2 = 2/3*N + 6 etc.
    We now try and compare each case to each other.
    a > b as:
    2N + 2 > 2N / 2 + 4. But our pattern also meets the following
    condition: B < A. We don't consider the other half of the set, where B > A, because multiplication is commutative.
    Which means A * B = B * A.
    So, because B < A, case b means 2 < N / 2. Going back, we get 2N > N + 2. But as we agreed that 2 < N,
    2N > N + 2 is always true (qed).
    b > c
    2N / 2 + 4 > 2N / 3 + 6
    N > 2N/3 + 2
    The only way 2N/3 + 2 = N is if 2 = N/3;
    but 3 < N/3 (B < A), and 2 < 3, so 2 < N/3.
    So, 2N/2 + 4 > 2N/3 + 6 is always true (qed).
    ...
    so each case following will necessarily give a perimeter smaller than the one before.

    3. Conclusion: the smallest perimeter is the one for the largest B, where B < A. This is where B < sqrt(N) and
    A > sqrt(N).
    '''
    area = N
    if area == 1:
        return 4
    for i in range(int(math.sqrt(area)), area + 1):
        if area % i == 0:
            sideA = area / i
            sideB = i
            break
    perimeter = int(2 * (sideA + sideB))
    return perimeter

t = logging.debug('start')
result = solution(36)
t1 = logging.debug('end')
print(result)
