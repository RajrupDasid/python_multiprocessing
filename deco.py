import time

def time_calculate(func):
    def time_func(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end =  time.time()
        print("Total time was taken to perform the work ::",func.__name__, end - begin)
    return time_func
