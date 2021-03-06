import numpy as np
import glob
import re
import os
import os.path
from tqdm import tqdm
import datetime
import string
import nltk
import itertools

punctuation = string.punctuation.replace(".", "")
files = np.array(glob.glob('../data/TimesOfIndiaData/2012/*.txt'))

if os.path.isfile('../data/TimesOfIndia/2012/05-Sep-47401.txt'):
    os.remove('../data/TimesOfIndia/2012/05-Sep-47401.txt')

A = {}
B = {}
C = {}
fileData = {}
for fileName in tqdm(files):
    with open(fileName) as f:
        fullText = f.read()
        pubDate = datetime.datetime.strptime(fullText.split("\n")[0], "%b-%d-%Y").date()
        fullText = fullText.replace("\n", " ")
        place = re.findall(r"\b([A-Z]+)\b:", fullText)
        if place:
            body = fullText.partition(place[0] + ": ")[2]
            body = body.translate(None, punctuation)
            shortName = fileName.replace("../data/TimesOfIndiaData/2012/", "")
            fileData[shortName] = [pubDate, body] #TODO remove
			lines = body.split(". ")
			for line in lines:
				words = nltk.word_tokenize(line)
				#get unique words
				unique_words = list(set(words))
				
				for word in unique_words:
					if not A[word]: A[word] = 1   #count of sentences for a word c_i
					else: A[word] += 1
				#now for neighbours of i
				
				#for i,word in unique_words:
				#i = iter(unique_words)
				#next_word = i.next()
					
					for subset in itertools.combinations(unique_words,2):
						if not B[word]: B[word] = 1
						else: B[word] += 1
				#count of sentence where both the words are co-occuring 
				

# # get the file sizes for all files in kB
# fileSizes = np.array([os.stat(files[i]).st_size for i in range(len(files))])/1000.0

# # find indices of elements where there are no placenames
# considered only files that have place names in them; although
# this eliminates certain large documents, this can be used. the docs
# that were removed are actually descriptive ones.

# stop words
# string.punctuation - "."
