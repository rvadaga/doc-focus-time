import numpy as np
import glob
import re
import os
import os.path
from tqdm import tqdm
import datetime
import string

punctuation = string.punctuation.replace(".", "")
files = np.array(glob.glob('../data/TimesOfIndiaData/2012/*.txt'))

if os.path.isfile('../data/TimesOfIndia/2012/05-Sep-47401.txt'):
    os.remove('../data/TimesOfIndia/2012/05-Sep-47401.txt')

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
            fileData[shortName] = [pubDate, body] 

# # get the file sizes for all files in kB
# fileSizes = np.array([os.stat(files[i]).st_size for i in range(len(files))])/1000.0

# # find indices of elements where there are no placenames
# considered only files that have place names in them; although
# this eliminates certain large documents, this can be used. the docs
# that were removed are actually descriptive ones.

# stop words
# string.punctuation - "."
