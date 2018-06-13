import random
import datetime

R1_CPU_TIME = []

now = datetime.datetime.now()

for i in range(-12,13):
    time = (datetime.datetime.now() + datetime.timedelta(hours=i))
    R1_CPU_TIME.append((time,random.randint(1,100)))

print(R1_CPU_TIME)


R2_CPU_TIME = []

now = datetime.datetime.now()

for i in range(-12,13):
    time = (datetime.datetime.now() + datetime.timedelta(hours=i))
    R2_CPU_TIME.append((time, random.randint(0, 100)))

print(R2_CPU_TIME)




