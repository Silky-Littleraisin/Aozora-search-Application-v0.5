import re
import numpy as numpy
import scipy as sp 
import bz2

fname_input='enwiki-20150112-400-r10-105752.txt.bz2'
fname_out='corpus_80.txt'

with bz2.open(fname_input,'rt') as data_file, open(fname_out,'wt') as output_file:
    for line in data_file:
        tokens=[]
        for chunk in line.split(''):
            token