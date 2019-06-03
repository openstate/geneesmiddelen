#!/usr/bin/env python

import sys
import os
import re
from glob import glob
from pprint import pprint
import json

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
    cur = None
    n = 0
    p = 0
    for t in tables:
        for r in t.xpath('./table/tbody/tr'):
            # if u''.join(r.xpath('.//td//text()')).strip() == 'Productgroep':
            cell_text = u''.join(r.xpath('./td[1]//text()')).strip()
            if cell_text == 'Productgroep':
                n += 1
                if cur is not None:
                    result.append(cur)
                cur = {
                    'Productgroep': None,
                    'Maximumprijs': None,
                    'Eenheid': None,
                    'Artikelen': []
                }
                p = 0
                continue
            if cur is None:
                continue
            if p == 0:  # Productgroep
                cur['Productgroep'] = cell_text
                p += 1
            if p == 1:  #Maximumprijs
                cell_text = u''.join(r.xpath('./td[2]//text()')).strip()
                if ' per ' in cell_text:
                    price, unit = cell_text.split('per', 1)
                else:
                    unit = 'Onbekend'
                    price = cell_text.replace(' per', '')
                cur['Maximumprijs'] = price.strip()
                cur['Eenheid'] = unit.strip()
                p += 1
                continue
            if p == 2 and cell_text == 'Registratienummer':
                p += 1
                continue
            if p == 3 and cell_text != '':
                cur['Artikelen'].append({
                    'Registratienummer': cell_text,
                    'Artikelnaam': u''.join(r.xpath('./td[2]//text()')).strip()
                })
    return result

def main(argv):
    file_paths = get_files()
    for file_path in sorted(file_paths):
        print(file_path)
        data = _parse_file(file_path)
        json_path = file_path.replace('.html', '.json')
        with open(json_path, 'w') as out_file:
            json.dump(data, out_file)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
