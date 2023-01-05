import logging
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


n = random.randrange(1, 1000000, 2)
print('Number of elements in array', n, type(n))
arr = []
n = 17
elem = random.randrange(1, 1000000000)
arr.append(elem)

for i in range(n - 1):
    elem = random.randrange(1, 1000000000)
    arr.append(elem)
    # How many copies should it have? 1 or ... max uneven. Uneven because original + uneven no of copies gives an even
    # number of elements.
    my_iterator = [1]
    max_even = random.choice(range(2, n-2, 2))
    print('max even is', max_even)
    for i in range(2, max_even, 2):
        my_iterator.append(i)
    print(my_iterator)
    for i in my_iterator:

        elem_copy = elem
        arr.append(elem_copy)

print(arr)
