# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])


html = "\n".join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
