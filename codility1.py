from random import randrange


def solution(N):
    x_bin = bin(N)
    x_bin = x_bin[2:]
    print(len(x_bin), 'len', x_bin)
    consec_list = []
    for i in range(len(x_bin) - 1):
        print('position {} equal to {} enters the scene.'.format(i, x_bin[i]))
        if len(consec_list) > 0:
            if i < (i - 1 + consec_list[-1]):
                print('and leaves the scene')
                continue
        consec = 0
        while x_bin[i] == x_bin[i+1] == str(0):
            print('in while')
            consec += 1
            i = i + 1
            # If this is the last digit, break.
            if i == (len(x_bin) - 1):
                if x_bin[i] == '0':
                    consec = 0
                break
        if i != len(x_bin) - 1:
            print(i, 'in final filter')
            # If this is a lonely zero, with nothing after it.
            if x_bin[i] == str(0) and x_bin[i+1] != '0':
                consec_list.append(1)
            # If we have some count going for consecutives.
            elif consec != 0:
                consec_list.append(consec + 1)
            print(consec_list)
    consec_list.sort()
    if len(consec_list) > 0:
        result = consec_list[-1]
    else:
        result = 0
    # if len(consec_list) > 0:
    #     if consec_list[-1] != 1:
    #         result = consec_list[-1]
    #     else:
    #         result = 0
    # else:
    #     result = 'no zeros'
    return f'lenght of longest sequence is {result}'


number_ = randrange(1, 2147483648)

print(solution(1041))

