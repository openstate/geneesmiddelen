#!/usr/bin/env python

import sys
import os
import re
from glob import glob
from pprint import pprint

import requests

def get_files():
    return glob('../data/*.html')

def _parse_file(file_path):
    pass


def main(argv):
    file_paths = get_files()
    for file_path in file_paths:
        print(file_path)
        _parse_file(file_path)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
