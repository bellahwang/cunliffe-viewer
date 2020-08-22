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
                for p in entry.findall(".//TEI:p", ns):
                    for gloss in p.findall(".//TEI:gloss", ns):
                        glosstxt = gloss.text
                        print('Gloss: ' + glosstxt)
                    for bibl in p.findall(".//TEI:bibl", ns):
                        biblcite = bibl.get('n')
                        if (inputCite == biblcite):
                            print(biblcite)
                            homerwork = biblcite[5:7]
                            returnWorks(inputWord, inputCite, homerwork)
                        else:
                            print(biblcite)
                            homerwork = biblcite[5:7]
                            returnWorks(inputWord, biblcite, homerwork)
                        
def hompers(inputWord, inputCite):
    
    FILENAME = "cunliffe.hompers.unicode.xml"
    tree = ET.parse(FILENAME)
    root = tree.getroot()

    for entry in root.findall(".//TEI:div[@type='textpart']", ns):
        lemma = entry.get('n')
        if (lemma != None):
            if (lemma  == inputWord):
                for p in entry.findall(".//TEI:p", ns):
                    for gloss in p.findall(".//TEI:gloss", ns):
                        glosstxt = gloss.text
                        print('Gloss: ' + glosstxt)
                    for bibl in p.findall(".//TEI:bibl", ns):
                        biblcite = bibl.get('n')
                        if (inputCite == biblcite):
                            homerwork = biblcite[5:7]
                            print(biblcite)
                            returnWorks(inputWord, inputCite, homerwork)
                        else:
                            homerwork = biblcite[5:7]
                            print(biblcite)
                            returnWorks(inputWord, biblcite, homerwork)

print("This script is a tool to query for lemmas and their citations in the Cunliffe Lexicon.")
print("Results will be outputted as 'gloss' '-> citations underneath gloss'.")
print("If no citation is inputted, all known citations will be outputted.")
print('\n')

print("Enter lemma.")
inputWord = input("Input: ")

print("Enter citation in the format of 'Hom. Il. 4.233', 'Hom. Od. 3.22', etc. If you would not like to input a citation, input 'N/A'.")
inputCite = input("Input: ")
print("")

print("LexEntries results: " + '\n')
lexentries(inputWord, inputCite)

print("HomPers results: " + '\n')
hompers(inputWord, inputCite)
