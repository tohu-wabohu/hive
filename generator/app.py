import time

while True:
    t = time.time()

    print(time.strftime('%Y-%m-%d %H:%M:%S %Z', time.localtime(time.time())))

    time.sleep(5)
