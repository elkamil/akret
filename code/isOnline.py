import os
hostname = "8.8.8.8"


def isOnline():
    response = os.system("timeout 0.5 ping -c 1 " + hostname)
    if response == 0:
        return True
    else:
        return False
