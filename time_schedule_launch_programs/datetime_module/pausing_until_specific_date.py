import datetime, time

halloween_2029 = datetime.datetime(2029, 10, 31, 0, 0, 0)

while datetime.datetime.now() < halloween_2029:
    time.sleep(1) # wait 1sec before loop check again
