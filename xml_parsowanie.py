from xml.dom.minidom import parse
import xml.dom.minidom

domTree = xml.dom.minidom.parse('test.xml')
collection = domTree.documentElement
if collection.hasAttribute("shelf"):
    print("ROOT: %s" % collection.getAttribute("shelf"))

movies = collection.getElementsByTagName('movie')

for m in movies:
    print("***FILMY***")
    if m.hasAttribute("title"):
        print("Tytuł: %s" % m.getAttribute("title"))

    type = m.getElementsByTagName('type')[0]
    print("Typ: %s" % type.childNodes[0].data)
