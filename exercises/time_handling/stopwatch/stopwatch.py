from time import time

print('Started!')

start_time = time()
last_time = start_time
lap = 1

try:
    while True:
        input()
        lap_time = round(time() - last_time,2)
        total_time = round(time() - start_time, 2)
        print(f'lap #{lap}: {total_time} ({lap_time})', end='')
        lap += 1
        last_time = time()
except KeyboardInterrupt:
    print('\nDone')