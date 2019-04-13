import nltk,pdb, pandas as pd,sys,numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile

""" Converts and excel spreadsheet of words into an excel spreadsheet of cmu transcriptions

To run in the terminal, type

	python3 cmu.py FILENAME

where filename is something like "mysheet.xlsx" (no quotes)
It will return a file called transcribed.xlsx"""

try:
    cmu = nltk.corpus.cmudict.dict()
except LookupError:
    nltk.download('cmudict')
    cmu = nltk.corpus.cmudict.dict()


words = np.array(pd.read_excel(sys.argv[1]).fillna(''))


bad = '-undefined-'

def transcribe (word):
	try:
		return(' '.join(cmu[word.lower()][0]))
	except KeyError:
		if word=='':
			return('')
		else:
			return(bad)

f = np.vectorize(transcribe,otypes=['object'])

transcribed = pd.DataFrame(f(words))

writer = ExcelWriter('transcribed.xlsx')
transcribed.to_excel(writer,'Sheet1',index=False)
writer.save()