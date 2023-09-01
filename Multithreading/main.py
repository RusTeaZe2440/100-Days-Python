import threading
import time

def func(seconds):
    time.sleep(seconds)
    print(f"waited for {seconds} seconds")
time1 = time.perf_counter()
# func(5)
# func(4)
# func(2)

t1 = threading.Thread(target=func, args=[3])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time2 = time.perf_counter()
Executiontime = (time2 - time1)
print(Executiontime)


#  threadpool executor learn more about in concurrent.futures it is more used in real world projects.

