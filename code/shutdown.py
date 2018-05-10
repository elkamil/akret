#skrypt do zatrzymywania systemu
import os


def shutdown():
    os.system("sudo /sbin/shutdown now")
