import sys
import os
# sys.path.append(os.getcwd())

import time
print(os.getcwd())
# time.sleep(300)
from functions.src import goodbye


def main(context):
    print("hello world")
    goodbye.bye()