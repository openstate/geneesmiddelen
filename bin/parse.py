#!/usr/bin/env python

import sys
import os
import re
from glob import glob
from pprint import pprint

import requests
from lxml import etree

def get_files():
    return glob('../data/*.html')

def _parse_file(file_path):
    with open(file_path) as in_file:
        content = in_file.read()
    html = etree.HTML(content)
    tables = html.xpath('//div[@class="table--container"]')
    result = []
    n = 0
    for t in tables:
        for r in t.xpath('./table/tbody/tr'):
            # if u''.join(r.xpath('.//td//text()')).strip() == 'Productgroep':
            cell_text = u''.join(r.xpath('./td[1]//text()')).strip()
            if cell_text == 'Productgroep':
                n += 1
    print(n)

def main(argv):
    file_paths = get_files()
    for file_path in sorted(file_paths):
        print(file_path)
        _parse_file(file_path)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
