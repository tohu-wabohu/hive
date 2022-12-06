import time

while True:
    t  = time.time()
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

    print(ts)

    time.sleep(5)
