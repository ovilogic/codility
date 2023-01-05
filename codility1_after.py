import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


from random import randrange


def solution(N):
    x_bin = bin(N)
    x_bin = x_bin[2:]
    consec_list = []
    for i in range(len(x_bin) - 1):
        consec = 0
        while x_bin[i] == x_bin[i+1] == str(0):
            consec += 1
            i = i + 1
            if i == (len(x_bin) - 1):
                consec = 0
                break
        consec_list.append(consec + 1)
    consec_list.sort()
    if consec_list[-1] != 1:
        result = consec_list[-1]
    else:
        result = 0
    return result


print(solution(1))