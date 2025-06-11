# Structure File using DSSR

import requests
import os
import sys
from os.path import isfile


dir= os.getcwd()
count=0

for filename in os.listdir('.'):
    if filename.endswith('.cif'):
        count +=1
        print (count)
        pname= filename[:4]+'-dssr.json'
        x= dir+'/'+filename[:4]+'-dssr.json'
        if isfile(x)== True:
            print ('ALREADY CHARACTERIZED')
        else:
            print ('NOT CHARACTERIZED YET')
            print (filename)
            os.system('./x3dna-dssr -i='+filename+ ' --json'+' -o='+ filename[:4]+'-dssr.json')
            for f in os.listdir('.'):
                if f.startswith('dssr-'):
                    os.remove(f)
