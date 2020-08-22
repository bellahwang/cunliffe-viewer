from iliadodyssey import returnWorks
import xml.etree.ElementTree as ET

ns = {"TEI": "http://www.tei-c.org/ns/1.0"}

def lexentries(inputWord, inputCite):
    
    FILENAME = "cunliffe.lexentries.unicode.xml"
    tree = ET.parse(FILENAME)
    root = tree.getroot()

    for entry in root.findall(".//TEI:div[@type='textpart']", ns):
        lemma = entry.get('n')
        if (lemma != None):
            if (lemma  == inputWord):
                print(lemma)
                for subentry in entry.findall("./TEI:div", ns):
                    for p in subentry.findall("./TEI:p", ns):
                        for gloss in p.findall(".//TEI:bibl/../TEI:gloss", ns):
                            glosstxt = gloss.text
                            print(glosstxt)
                        for bibl in p.findall(".//TEI:bibl", ns):
                            biblcite = bibl.get('n')
                            if (inputCite == biblcite):
                                homerwork = biblcite[5:7]
                                returnWorks(inputWord, inputCite, homerwork)
                                print()
                        

                    
print("Enter lemma.")
inputWord = input("Input: ")

print("Enter cite. If there is no cite, input 'None'.")
inputCite = input("Input: ")
print("")

lexentries(inputWord, inputCite)