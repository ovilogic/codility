import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

L = [3, 1, 4, 1]
L2 = [3, 1, 4, 1, 5, 9]


def solution(l):
    x = ''
    l.sort(reverse=True)
    sum_ = 0
    for i in l:
        sum_ += i
    remnant_removed = False

    def wrap_up():
        if len(l) != 0:
            stringed = [str(i) for i in l]
            x = ''.join(stringed)
            y = int(x) % 3
            if y != 0:
                return 0
            else:
                return x
        else:
            return 0

    if sum_ % 3 == 0:
        wrap_up()
    else:
        quotients = [i for i in range(9) if i % 3 == 0]
        if sum_ % 3 == 1:
            for q in quotients:
                if q + 1 in l:
                    l.remove(q + 1)
                    print(l)
                    wrap_up()
                elif q + 2 in l:
                    l.remove(q + 2)
                    if q + 4 in l:
                        l.remove(q + 4)
                    elif q + 6 in l:
                        l.remove(q + 6)
                    wrap_up()

        elif sum_ % 3 == 2:
            for q in quotients:
                if q + 2 in l:
                    l.remove(q + 2)
                    remnant_removed = True
                    wrap_up()
            if not remnant_removed:
                for q in quotients:
                    if q + 1 in l:
                        l.remove(q + 1)
                    if 1 in l:
                        l.remove(1)
                        remnant_removed = True
                        wrap_up()
                    elif 2 in l:
                        l.remove(1)
                        remnant_removed = True
                        wrap_up()

    return wrap_up()


print(solution(L))
print(solution([9, 8, 2]))
print(solution(L2))
# for i in range(2000000000):
#     compulsion = [random.randint(0, 9) for i in range(9)]
#
#     print(solution(compulsion))
