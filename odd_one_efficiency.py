import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def odd_one_excelero(list_):
    x = [i for i in list_ if list_.count(i) % 2 != 0]
    return x[0]


def odd_one_efficient(list_):
    set_ = set(list_)
    list_copy = list_[:]
    for i in set(list_):
        list_copy.remove(i)
    print(list_copy)
    difference = list(set(list_) - set(list_copy))
    print('diff is', difference)
    return difference[0]


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

logging.debug('starts here')
print(odd_one_efficient(A))
# print(odd_one_excelero(A))
logging.debug('ends here')

