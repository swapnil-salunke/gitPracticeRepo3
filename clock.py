import time

while True:
    print(time.strftime("%H:%M:%S"), end="\r", flush=True)
    time.sleep(1)