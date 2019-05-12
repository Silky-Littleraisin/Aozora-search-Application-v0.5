import re

tuple=set()

with open('writer_name.txt') as file:
    lst=file.readlines()


for line in lst:
    tuple.add(line)

with open('writer_name_no_repeat.txt','w') as file:
    for line in tuple:
        file.write(line)
        file.write('\n')