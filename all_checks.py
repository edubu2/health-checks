#!/usr/bin/python3
import os
import shutil
import sys

def check_reboot():
    """Returns True if the PC has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_root_full():
    """Returns True if the root partition is full, False otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)

def main():
    checks = [
            (check_reboot, "Pending reboot"),
            (check_root_full, "Root partition full"),
    ]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)

    print("Everything ok.")
    sys.exit(0)
        
main()