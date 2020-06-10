# voynich
Python program finds all possible combinations of the known letters in the Voynich Manuscript and finds them in the manuscript.

## Abstract
The Voynich Manuscript is a text dated back to sometime during the 15th century. The mysterious document contains a foreign 
script and pictures of various plants, astrological symbols, and people. For hundreds of years, researchers have taken 
different approaches to deciphering the manuscript. One such approach is to find combinations of previously discovered letters 
in the manuscript taken from deciphered words, and locate these letter combinations in the manuscript. Locating combinations 
of known letters near images in the manuscript could provide a method of narrowing down the meanings of new words and, 
eventually, the meaning of the entire manuscript. 

The purpose of the letter combination algortihm is to find letter combinations that can be easily deciphered with reference to 
the images they describe.

## Files
- **datacaptions.rtf** - This text file includes only the lines on the manuscript that correspond to captions of images.
- **datanocounts.rtf** - This text file includes all lines in the manuscript.
- **testoutput.csv** - This is a csv file that contains letter combinations found in datacaptions.rtf for the letters 'T', 'h', 
'o', 'y', 'a', 'n', 'm', '9', '!' in the transliterated online version of the manuscript.
- **voyfinder.py** - This is the main file that includes all the logic.
