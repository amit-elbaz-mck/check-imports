import sys
import os
sys.path.append(os.getcwd())

from src.goodbye import bye

def main(context):
    print("hello world")
    bye()