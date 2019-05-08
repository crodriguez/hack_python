#import socket
import os
import sys
import platform
import subprocess
import sys
from datetime import datetime

ip = "172.16.100.175"   #input("Ingresa la IP:")
print platform.system()

listaPuertos = list(range(20, 200))

for puerto in listaPuertos:
    print puerto