# Use this one to run all the other scripts!

from cunliffeprocessing.cunliffelexentries import parseLexEntries
from cunliffeprocessing.cunliffehompers import parseHomPers

print("Enter a word to return the Cunliffe Lexicon entry for it.")
inputWord = input("Input: ")
print("")

print("Entries from cunliffe.lexentries.unicode.xml: ")
cunliffelexentries.parseLexEntries(inputWord)

print("")
print("Entries from cunliffe.hompers.unicode.xml: ")
cunliffehompers.parseHomPers(inputWord)

