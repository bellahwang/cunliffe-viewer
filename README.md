# cunliffe-viewer
A script to query for vocabulary lemmas and line numbers in the Cunliffe lexicon.

## How to Run 

To run on a command line, change into the directory with all files and run:
```bash
python3 cunliffe.py
```

To run on Spyder, open cunliffe.py and run the script using the green arrow button.

## Usage

After running the script, the following text will appear.
```
This script is a tool to query for lemmas and their citations in the Cunliffe Lexicon.
Results will be outputted as 'gloss' '-> citations underneath gloss'
If no citation is inputted, all known citations will be outputted.
Enter lemma.
Input: 
```

In other words, all citations referenced by its gloss will be underneath its respective gloss.

Next, type in a lemma of your choice and hit enter.
```
Enter lemma. 
Input: μῆνις
```

After hitting enter, the script will output the following text. 'work', 'book', or 'line' can be specified.
Examples of possible citations 
```
Would you like to search by work (Hom. Il., Hom. Od.),
by book (Hom. Il. 1, Hom Od. 1), or line number? (Hom. Il. 1.1, Hom. Od. 1.1)
Enter 'work', 'book', or 'line'.
Input:
```

Depending on the selection you make, the following text will vary in terms of content in the square brackets. 
The square brackets list possible examples and formats that the citations should be inputted in.
If you want all citations underneath each gloss within the Cunliffe Lexicon instead of a specific citation, input 'N/A'.
```
Enter citation in the format of [varies with selection of 'work', 'book', or 'line']. 
If you would not like to input a citation, input 'N/A'.
Input: N/A
```
The script will then output all known citations of the lemma in the Cunliffe Lexicon. 
```
LexEntries results: 

Gloss: Wrath, ire :
Hom. Il. 1.1
μῆνιν ἄειδε θεὰ Πηληϊάδεω Ἀχιλῆος οὐλομένην , ἣ μυρί' Ἀχαιοῖς ἄλγε' ἔθηκε , πολλὰς δ' ἰφθίμους ψυχὰς Ἄϊδι προΐαψεν ἡρώων , αὐτοὺς δὲ ἑλώρια τεῦχε κύνεσσιν οἰωνοῖσί τε πᾶσι , Διὸς δ' ἐτελείετο βουλή , ἐξ οὗ δὴ τὰ πρῶτα διαστήτην ἐρίσαντε Ἀτρεΐδης τε ἄναξ ἀνδρῶν καὶ δῖος Ἀχιλλεύς . 
Sing, goddess, about the wrath of Peleus' son, Achilles, a killing wrath. It imposed countless suffering upon the Achaeans. It dispatched to Hades many valiant souls of heroes. It made them themselves spoil for dogs and every bird. The plan of Zeus came to be fulfilled. From the time when first they parted in strife Atreus' son, king of men, and brilliant Achilles. 

Hom. Il. 1.75
ὦ Ἀχιλεῦ κέλεαί με Διῒ φίλε μυθήσασθαι μῆνιν Ἀπόλλωνος ἑκατηβελέταο ἄνακτος · [0] [1] 
Achilles, dear to Zeus, you order me to declare the wrath of Apollo, the lord who strikes from afar. 
...
```

or

```
Enter citation in the format of [varies with selection of 'work', 'book', or 'line']. 
If you would not like to input a citation, input 'N/A'.
Input: Hom. Il. 9.517
```
The script will only return the inputted instance of the lemma, if it exists.
```
LexEntries results: 

Gloss: Wrath, ire :
Hom. Il. 9.517
εἰ μὲν γὰρ μὴ δῶρα φέροι τὰ δ' ὄπισθ' ὀνομάζοι Ἀτρεΐδης , ἀλλ' αἰὲν ἐπιζαφελῶς χαλεπαίνοι , οὐκ ἂν ἔγωγέ σε μῆνιν ἀπορρίψαντα κελοίμην Ἀργείοισιν ἀμυνέμεναι χατέουσί περ ἔμπης · 
For if the son of Atreus were not offering thee gifts and telling of yet others hereafter, but were ever furiously wroth, I of a surety should not bid thee cast aside thine anger and bear aid to the Argives even in their sore need. 
```
