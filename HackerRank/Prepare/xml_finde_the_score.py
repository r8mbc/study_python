# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true


import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    a = 0
    for i in node.iter():
        a += sum([len(i.attrib)])
    return a


if __name__ == "__main__":
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
