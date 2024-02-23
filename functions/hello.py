import sys
import os
# sys.path.append(os.getcwd())

import time
print(os.getcwd())
print(sys.path)
# time.sleep(300)
from functions.src import goodbye


def main(context):
    print("hello world")
    goodbye.bye()