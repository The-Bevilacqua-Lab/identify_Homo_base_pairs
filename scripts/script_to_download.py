import os
import pandas as pd
from subprocess import call


#import list of structures to be downloaded
df_str= pd.read_csv('/storage/work/jlj5912/NMR_Structures/All_NMR_Structures.csv')
home= os.getcwd()
str_files=[]
str_dir= '/storage/work/jlj5912/NMR_Structures' #directory where we want to save the structures
os.chdir(str_dir)

for i, j in enumerate(df_str['PDB_ID']):
    str_files.append(j)

#downloading the structures
for filename in str_files:
    full_path= os.path.join(str_dir, filename+'.cif')
    if os.path.isfile(full_path):
        print ('FILE ALREADY EXISTS! NOT DOWNLOADING!')
    else: 
        print ('Downloading '+ filename)
        url = "http://www.rcsb.org/pdb/files/%s.cif" %filename
        call (["curl","-L","-O","-s",url])

os.chdir(home)