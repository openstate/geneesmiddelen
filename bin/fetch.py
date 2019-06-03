#!/usr/bin/env python

import sys
import os
import re
from pprint import pprint
from time import sleep

import requests

def get_urls():
    data = []
    with open("../urls.txt") as in_file:
        data = in_file.readlines()
    return [l.strip() for l in data]


def _download_url(url):
    file_path = '../data/%s.html' % (url.split('/')[-1],)
    r = requests.get(url)
    if r.status_code < 200 or r.status_code >= 300:
        return
    with open(file_path, 'wb') as out_file:
        out_file.write(r.content)

def main(argv):
    urls = get_urls()
    for url in urls:
        print(url)
        _download_url(url)
        sleep(1)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
