import sys
import xml.etree.ElementTree as ET

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}

def printIlEngSent(targetSentID):
    
    FILENAME = "atmurray.iliad-sentalign-copy.xml"
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    
    for s in root.findall(".//TEI:s", ns):
        id = s.get('{http://www.w3.org/XML/1998/namespace}id')
        if (targetSentID == id[4:11]):
            sys.stdout.write(s.text)

def printOdEngSent(target):
    
    FILENAME = "atmurray.odyssey-sentalign-copy.xml"
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    
    for s in root.findall(".//TEI:s", ns):
        id = s.get('{http://www.w3.org/XML/1998/namespace}id')
        if (target == id[4:11]):
            sys.stdout.write(s.text)