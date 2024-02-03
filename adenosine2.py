import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


L = [3, 1, 4, 1]
L2 = [3, 1, 4, 1, 5, 9]


def solution(l):
    x = ''
    l.sort(reverse=True)
    sum_ = 0
    for i in l:
        sum_ += i

    def wrap_up():
        if len(l) != 0:
            stringed = [str(i) for i in l]
            x = ''.join(stringed)
            y = int(x) % 3
            if y != 0:
                return 0
            else:
                return str(int(x))
        else:
            return 0

    if sum_ % 3 == 0:
        wrap_up()
    else:
        if sum_ % 3 == 1:
            if 1 in l:
                l.remove(1)
                wrap_up()
            elif 4 in l:
                l.remove(4)
                wrap_up()
            elif 7 in l:
                l.remove(7)
                wrap_up()
            elif 2 in l:
                l.remove(2)
                if 5 in l:
                    l.remove(5)
                    wrap_up()
                elif 8 in l:
                    l.remove(8)
                    wrap_up()

        elif sum_ % 3 == 2:
            if 2 in l:
                l.remove(2)
                wrap_up()
            elif 5 in l:
                l.remove(5)
                wrap_up()
            elif 8 in l:
                l.remove(8)
                wrap_up()
            elif l.count(1) >= 2:
                l.remove(1)
                l.remove(1)
                wrap_up()
            elif 4 in l:
                l.remove(4)
                if 1 in l:
                    l.remove(1)
                elif 2 in l:
                    l.remove(2)
                wrap_up()
            elif 7 in l:
                l.remove(7)
                if 1 in l:
                    l.remove(1)
                elif 2 in l:
                    l.remove(2)
                wrap_up()
            else:
                return 0

    return wrap_up()


print(solution(L))
print(solution([9, 2, 5]))
print(solution(L2))