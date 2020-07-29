import shutil

def check_disk_storage(disk, min_absolute, min_percent):
    """Returns True if there is enough free disk space, False otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free GB
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

# Check for at least 2 GB and 10% free
if not check_disk_storage("/", 2*2*30, 10):
    print("ERROR: Not enough disk space.")
    return 1

print("Everything ok.")
return 0