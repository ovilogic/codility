import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')


def timer_decorator(f):
    st = time.perf_counter_ns()
    print(f)
    et = time.perf_counter_ns()
    print(et, st, sep='\n')
    print(float((et - st) / 1000000000))
    return f


list_ = []
for i in range(100000):
    list_.append(i)


st = time.perf_counter_ns()
for i in list_:
    pass
et = time.perf_counter_ns()
print(et, st, sep='\n')
print('simple iteration', float((et - st) / 1000000000))

st = time.perf_counter_ns()
while len(list_) > 1:
    list_.remove(list_[0])
et = time.perf_counter_ns()
print(et, st, sep='\n')
print('while iteration', float((et - st) / 1000000000))