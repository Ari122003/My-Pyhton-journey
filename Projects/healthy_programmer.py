from datetime import datetime
import time
from plyer import notification


def drink():
    notification.notify(title="Hello", message="Drink Water", timeout=1)

    with open("logs.txt", "a") as f:

        f.write("\nWATER:"+str(datetime.now()))


def eye():
    notification.notify(title="Hello", message="Do eye workout", timeout=1)

    with open("logs.txt", "a") as f:
        f.write("\nEYES:"+str(datetime.now()))


def phy():
    notification.notify(
        title="Hello", message="Do physical workout", timeout=1)

    with open("logs.txt", "a") as f:
        f.write("\nPHYSICAL:"+str(datetime.now()))


w_ini = time.time()
e_ini = time.time()
phy_ini = time.time()
water = 10
eye_ex = 15
phy_ex = 20

while True:

    if(time.time()-w_ini >= water):
        drink()
        w_ini = time.time()

    if(time.time()-e_ini >= eye_ex):
        eye()
        e_ini = time.time()

    if(time.time()-phy_ini >= phy_ex):
        phy()
        phy_ini = time.time()
