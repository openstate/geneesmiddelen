#!/usr/bin/env python

# https://wetten.overheid.nl/BWBR0008023/2019-04-20

import sys
import os
import re
from pprint import pprint
from time import sleep

import requests
from lxml import etree
from urllib.parse import urljoin

def get_urls(loc):
    html = etree.HTML(requests.get(loc).content)
    options = html.xpath('//div[@id="popupvergelijken"]//select/option')
    return [re.sub('_\d$', '', u''.join(x.xpath('./@value'))) for x in options]

def main(argv):
    if len(argv) > 1:
        loc = argv[1]
    else:
        loc = 'https://wetten.overheid.nl/BWBR0008023/'
    urls = get_urls(loc)
    for url in urls:
        print(urljoin(loc, url))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
