import lxml.etree as et
from lxml.etree import HTMLParser
from StringIO import StringIO 

def parse(self, response):
    parser = HTMLParser(encoding='utf-8', recover=True)
    tree = et.parse(StringIO(response.body), parser)
    for element in tree.xpath('//script'):
        element.getparent().remove(element)

    print et.tostring(tree, pretty_print=True, xml_declaration=True)
