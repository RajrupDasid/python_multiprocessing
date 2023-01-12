import math
from deco import time_calculate
import sys
from multiprocessing import Pool, Process

sys.set_int_max_str_digits(20000000)

@time_calculate
def factorial(num):
    print(math.factorial(num))

def multicpu():    
    t1 = Process(target=factorial,args=(1000000,))
    print(t1)
    t1.start()
    t1.join()
multicpu()
