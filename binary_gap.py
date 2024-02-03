#! python3
''' A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at
both ends in the binary representation of N.'''

import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


x = random.randrange(1, 2147483647)


def solution(N):
    b_ = bin(N)[2:]
    counts = []
    for i in range(len(b_) - 2):
        if b_[i] == '1':
            count = 0
            while b_[i + 1] != '1':
                count += 1
                i += 1
                if i == len(b_) - 1:
                    if b_[i] == '0':
                        count = 0
                        break
                    else:
                        break
            if count != 0:
                counts.append(count)

    if len(counts) != 0:
        counts.sort()
        print(counts)
        return counts[-1] 
    else:
        return 0



print(x, bin(x))
print(solution(x))
