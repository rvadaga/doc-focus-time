# coding: utf-8
import os
import glob
import numpy as np

# get an array of all file names in 2012 directory
files = np.array(glob.glob('../data/TimesOfIndiaData/2012/*.txt'))

# an array containing all file sizes (in kB)
fileSizes = np.array([os.stat(files[i]).st_size for i in range(len(files))])/1000.0

import matplotlib.pylab as mpl
f1 = mpl.figure(1)
mpl.hist(fileSizes, bins=90)
mpl.xlabel('file size in kilo bytes')
mpl.ylabel('number of files')
mpl.title('File sizes considering the entire corpus')
f1.savefig("hist_1kB.pdf")
f1.show()

f2 = mpl.figure(2)
mpl.hist(fileSizes[fileSizes <= 15], bins=np.arange(0, 15, 0.1))
mpl.xlabel('file size in kilo bytes')
mpl.ylabel('number of files')
mpl.title('File sizes considering the dense region')
f2.savefig("hist_0.1kB.pdf")
f2.show()

# indices where file size is between 200 and 1000
np.where((fileSizes <= 1000) & (fileSizes >200))[0]

# file names correpsonding to those indices
files[np.where((fileSizes <= 1000) & (fileSizes >200))[0]]

# number of files obeying the above mentioned criteria
len(files[np.where((fileSizes <= 1000) & (fileSizes >200))[0]])

