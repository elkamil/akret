import os
hostname = "onet.pl"


def isOnline():
    response = os.system("timeout 0.5 ping -c 1 " + hostname)
    if response == 0:
        return True
    else:
        return False
