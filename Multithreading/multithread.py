import threading
import time
def cube(num):
    print("cube is {}".format(num * num * num))

def square(num):
    time.sleep(2)
    print("square is {}".format(num * num))
    

if __name__ == "__main__":
    t1 = threading.Thread(target=cube, args=[10])
    t2 = threading.Thread(target=square, args=[10])

    t1.start()
    t2.start()

    t1.join()
    t2.join()