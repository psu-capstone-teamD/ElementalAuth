import xml.etree.ElementTree as ET
tree = ET.ElementTree(file='BXFsample.xml')

indent = 0
ignoreElems = ['displayNameKey', 'displayName']

def printRecur(root):
    """Recursively prints the tree."""
    if root.tag in ignoreElems:
        return
    print ' '*indent + '%s: %s' % (root.tag.title(), root.attrib.get('name', root.text))
    global indent
    indent += 4
    for elem in root.getchildren():
        printRecur(elem)
    indent -= 4

root = tree.getroot()
printRecur(root)