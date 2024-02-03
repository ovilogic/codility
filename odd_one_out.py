''' A non-empty array A consisting of N integers is given. The array contains an odd number of elements,
and each element of the array can be paired with another element that has the same value,
except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times. '''
import logging
import time


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def timer_decorator(f):

    def rapper(*args):
        st = time.perf_counter_ns()
        f(*args)
        et = time.perf_counter_ns()
        print(et, st, sep='\n')
        print(float((et - st) / 1000000000))

    return rapper

#
# @timer_decorator
# def solution(A):
#     A.sort()
#     if len(A) > 1:
#         for i in range(len(A) - 2):
#             while True:
#                 if len(A) > 2:
#                     if A[i] == A[i+1]:
#                         A.remove(A[i])
#                         A.remove(A[i])
#                     else:
#                         return A[i]
#                 else:
#                     return A[0]
#     else:
#         return A[0]


# @timer_decorator
# def faster(A):
#     A.sort()
#     A_set = set(A)
#     A_set = list(A_set)
#     for i in A_set:
#         if len(A) != 1 and A.index(i) != len(A) - 1 and A[A.index(i)] == A[A.index(i) + 1]:
#             A.remove(A[A.index(i)])
#             A.remove(A[A.index(i)])
#             continue
#         else:
#             return i

# @timer_decorator
# def while_faster(A):
#     for i in list(set(A)):
#         if A.count(i) % 2 == 0:
#             while id(i) in A:
#                 A.remove(i)
#
#         else:
#             return i

# arr = []
# x = 100000
# for i in range(x):
#     arr.append(i)
# for i in range(x):
#     arr.append(i)
# arr.append(x+1)
#
# print(len(arr))



# st = time.perf_counter_ns()
# print(solution(A))
# et = time.perf_counter_ns()
# print(et, st, sep='\n')
# print(float((et - st) / 1000000000))


@timer_decorator
def dict_shot(list_):

    for i in list_:
        cooly_scientific = list_.count(i)
        if cooly_scientific % 2 == 0:
            continue
        else:
            print(f'{i} is the culprit')
            return i


def linear(list_):
    list_.sort()
    print(list_)
    while True:
        print(A[0], A[1])
        if list_[0] == list_[1]:
            list_.remove(list_[0])
            list_.remove(list_[0])
        else:
            print(list_[0])
            return list_[0]


A = []
for i in range(9):
    A.append(i)
A[0] = 9
A[1] = 3
A[2] = 9
A[3] = 3
A[4] = 9
A[5] = 7
A[6] = 9
A[7] = 7
A[8] = 5
print(A)

# A = [3]

# print(dict_shot(A))
linear(A)