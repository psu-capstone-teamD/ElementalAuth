import xml.etree.ElementTree as ET

def main():
    xmlService = xmlConverterService()
    xmlService.bxftolive()

class xmlConverterService:

    def __init__(self):
        self.xmlFile = 'BXFsample.xml'
        self.indent = 0

    def bxftolive(self):

        tree = ET.parse(self.xmlFile)
        root = tree.getroot()
        printXML(root)

        for child in root:
            print(child.tag, child.attrib)
            for children in child:
                if not children.attrib:
                    print(children.tag, children.text)
                else:
                    print(children.tag, children.attrib)


    def printXML(root):
        print ' ' * indent + '%s: %s' % (root.tag.title(), root.attrib.get('name', root.text))
        global indent
        indent += 4
        for elem in root.getchildren():
            printXML(elem)
        indent -= 4

if __name__ == '__main__':
    main()