#!/usr/bin/env python3
#author id:135843233
import subprocess

def free_space():
     output = subprocess.check_output("df -h | grep '/$' | awk '{print $4}'",shell=True,universal_newlines=True)
     return output.strip()

if __name__ == '__main__':
    print(free_space())