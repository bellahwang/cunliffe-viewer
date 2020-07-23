# from .IliadOdyssey import iliadodyssey
import xml.etree.ElementTree as ET

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}

def parseHomPers(input):
    
    FILENAME = "cunliffe.hompers.unicode.xml"
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    
    for entries in root.findall(".//TEI:div[@type='entry']", ns):
        wordEntry = entries.get('n')
        if (wordEntry != None):
            for gloss in entries.findall('.//TEI:gloss', ns):
                if (input == wordEntry):
                    print("Gloss:", gloss.text)
    
def parseLexEntries(input):
    
    FILENAME = "cunliffe.lexentries.unicode.xml"
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    
    for entries in root.findall(".//TEI:div[@type='entry']", ns):
        wordEntry = entries.get('n')
        if (wordEntry != None):
            for gloss in entries.findall('.//TEI:gloss', ns):
                if (input == wordEntry):
                    print("Gloss:", gloss.text)
                    
