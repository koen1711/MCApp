from threading import Thread

def Thread2():
    for i in range(100000):
        for j in range(100000):
            for k in range(100000):
                pass

def Thread1():
    for i in range(100000):
        print(i)
        for j in range(100000):
            for k in range(100000):
                pass

def Thread3():
    for i in range(100000):
        for j in range(100000):
            for k in range(100000):
                pass

def Thread4():
    for i in range(100000):
        for j in range(100000):
            for k in range(100000):
                pass

def Thread5():
    for i in range(100000):
        print(i)
        for j in range(100000):
            print(j)
            for k in range(100000):
                print(k)


t1 = Thread(target=Thread1).start()
t2 = Thread(target=Thread2).start()
t3 = Thread(target=Thread3).start()
t4 = Thread(target=Thread4).start()
t5 = Thread(target=Thread5).start()

