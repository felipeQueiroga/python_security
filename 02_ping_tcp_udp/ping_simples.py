import os
import sys

def ping(host): 
    print("#" * 60)

    print("-" * 60)
    os.system('ping -n 4 {}'.format( host))
    print("-" * 60)


if __name__ == "__main__":  
    ping('www.google.com')
