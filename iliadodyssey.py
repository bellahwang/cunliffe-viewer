import englishalignment
import sys
import xml.etree.ElementTree as ET

def printGrkSent(inputWord, inputCite, homerWork):

    if (homerWork == "Il"):
        FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"
    elif (homerWork == "Od"):
        FILENAME ="tlg0012.tlg002.perseus-grc1.tb.xml"
        
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    
    for sentence in root.findall('.//sentence'):
        sentid = sentence.get('id')
        for word in sentence.findall('./word'):
            lemma = word.get('lemma')
            cite = word.get('cite')
            if (cite != None):
                strippedCite = "Hom. Il. " + cite[32:]
                strippedCite2 = "Il. " + cite[32:]
                if ((inputWord == lemma and inputCite == strippedCite) or (inputWord == lemma and inputCite == strippedCite2)):
                    return sentid

def returnWorks(inputWord, inputCite, homerWork):
    
    if (homerWork == "Il"):
        FILENAME = "tlg0012.tlg001.perseus-grc1.tb.xml"
    elif (homerWork == "Od"):
        FILENAME ="tlg0012.tlg002.perseus-grc1.tb.xml"
        
    tree = ET.parse(FILENAME)
    root = tree.getroot()
    
    targetid = printGrkSent(inputWord, inputCite, homerWork)
    for sentence in root.findall('.//sentence'):
        sentid = sentence.get('id')
        if (sentid == targetid):
            for word in sentence.findall('./word'):
                form = word.get('form')
                lemma = word.get('lemma')
                if (inputWord == lemma):
                                     #  bold        green               end
                    sys.stdout.write('\033[1m' + '\33[32m' + form + '\033[0m')
                    sys.stdout.write(" ")
                else:
                    sys.stdout.write(form)
                    sys.stdout.write(" ")
    print("")
    if (homerWork == "Il"):
        englishalignment.printIlEngSent(targetid)
    elif (homerWork == "Od"):
        englishalignment.printOdEngSent(targetid)
    