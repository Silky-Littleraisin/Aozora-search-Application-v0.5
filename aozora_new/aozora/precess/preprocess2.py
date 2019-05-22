import os
import re

path = '/Users/silky/Documents/GitHub/textnovel/txt/'


for r, d, f in os.walk(path):
    for file in f:
        file = path + '/' + file
        with open(file) as novel:
            noveltext=novel.readlines()


