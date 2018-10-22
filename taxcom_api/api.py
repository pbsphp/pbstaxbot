# coding: utf-8

import os
import requests

from io import StringIO
from lxml import etree


URL = 'http://receipt.taxcom.ru/v01/show'


def _request(fp, s):
    """Download html page by fp and s params.
    """
    req = requests.get(URL, {'fp': fp, 's': s})

    if req.status_code != 200:
        raise RuntimeError(
            f'Request to {URL} (fp={fp}&s={s}) failed. HTTP {req.status_code}')

    return req.text


def _transform_from_html(html_text):
    """Transform HTML string to XML tree.
    """
    tree = etree.parse(
        StringIO(html_text),
        etree.HTMLParser()
    )

    my_path = os.path.dirname(os.path.abspath(__file__))
    xslt_path = os.path.join(my_path, 'template.xsl')

    with open(xslt_path, 'r') as f:
        xsl_tree = etree.parse(f)

    transform = etree.XSLT(xsl_tree)

    return transform(tree)


def _tree_to_obj(tree):
    """Return list with items by transformed XML tree.
    """
    items = []
    for item in tree.findall('/item'):
        items.append({
            'name': item.findtext('name').strip(),
            'price': item.findtext('price').strip(),
        })

    return items


def get(fp, s):
    """Get info by `fp' and `s' params.
    """
    html = _request(fp, s)
    tree = _transform_from_html(html)
    items = _tree_to_obj(tree)
    return items


if __name__ == '__main__':
    import re

    fp = input('FP: ')
    s = input('S: ')

    if not re.match(r'^\d{10}$', fp):
        print(f'Warning: {fp} does not match \\d{{10}}.')

    if not re.match(r'^\d+(\.\d{1,2})?$', s):
        print(f'Warning: {s} does not match \\d+(\\.\\d{{1,2}})?.')

    for item in get(fp, s):
        print('{name}: {price}'.format(**item))
