#! python3
from os import popen

cmd = "ifconfig | grep ether -m 1 | awk '{print $2}'"  # assume the first interface
print(popen(cmd).read().strip())
