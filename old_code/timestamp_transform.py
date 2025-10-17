import time

timeStamp = 1743061500000
print(1743061500000)
timeStamp /= 1000
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

timestamp_ms = int(time.time() * 1000)
print(timestamp_ms)