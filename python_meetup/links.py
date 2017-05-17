
import urllib
import urllib.request
import sys
from html.parser import HTMLParser

url = 'http://en.wikipedia.org/wiki/London'

def content_of_page(page):
    url = 'https://en.wikipedia.org/wiki/' + page
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    return content

def href_of_attrs(attrs):
    for (name, value) in attrs:
        if name == 'href':
            return value
    return None

def links_of_content(content):
    links = set()

    class LinksParser(HTMLParser):
        def handle_starttag(self,tag,attrs):
            if tag == 'a':
                href = href_of_attrs(attrs)
                links.add(href)
    links_parser = LinksParser()
    links_parser.feed(content)
    return links




# Read argument from command line
c1 = content_of_page(sys.argv[1])
l1 = links_of_content(c1)
c2 = content_of_page(sys.argv[1])
l2 = links_of_content(c2)

print(l1 & l2)

