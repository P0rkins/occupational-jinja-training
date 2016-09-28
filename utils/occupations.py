#Big L's occupation stuff

import random


#helper functions
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def store():
    inStream = open('~/data/occupations.csv','r')
    occupation = inStream.readlines()
    inStream.close()
    dic = {}
    for data in occupation:
        stripped = data.rstrip() #stripped data of /n
        temp = stripped.split(',')
        if is_number(temp[1]):
            dic[temp[0]] = float(temp[1]) 
    dic.pop('Total', None)
    dic.pop('Job Class', None)
    return dic

def randomize():
    return random.choice(occupations.keys())

#end helper functions
