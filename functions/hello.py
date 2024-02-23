import sys
import os
sys.path.append(os.getcwd())

import time

time.sleep(300)
from src.goodbye import bye

def main(context):
    print("hello world")
    bye()