# look for all drives in the computer first
import string
from ctypes import windll
import shutil
import os

def all_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives


def working_drives(dr):
    working = []
    for d in dr:
        try:
            shutil.disk_usage(d+':/')
            working.append(d)
        except:
            pass
    return working

def get_drives():
    return working_drives(all_drives())