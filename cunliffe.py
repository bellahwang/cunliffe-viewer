# Use this one to run all the other scripts!

from CunliffeProcessing.CunliffeEntries import hompersLexentries

print("Enter a word to return the Cunliffe Lexicon entry for it.")
inputWord = input("Input: ")
print("")

print("Entries from cunliffe.lexentries.unicode.xml: ")
hompersLexentries.parseLexEntries(inputWord)

print("")
print("Entries from cunliffe.hompers.unicode.xml: ")
hompersLexentries.parseHomPers(inputWord)

