import sys
import xml.etree.ElementTree as ET

sys.path.append("C:\Users\bella\Documents\GitHub\cunliffe-viewer\data")
# change FILENAME to local path
FILENAME = "atmurray.iliad-sentalign-copy.xml"

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}
tree = ET.parse(FILENAME)
root = tree.getroot()

def printEngSent(target):
	for s in root.findall(".//TEI:s", ns):
		id = s.get('{http://www.w3.org/XML/1998/namespace}id')
		if (target == id[4:11]):
			sys.stdout.write(s.text)
