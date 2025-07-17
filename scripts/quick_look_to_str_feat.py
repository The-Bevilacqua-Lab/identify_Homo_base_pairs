#this script can be used to have a quick look of the structural features of the structure of interest
#the script will ask for the PDB_ID (case does not matter here) and code for the structural features
#0= bp_pairs, 1=hbonds, 2= stacks

import os
import pandas as pd
import csv
import json
import numpy as np

def extract_info_from_json(P, dr):
    home= os.getcwd()
    os.chdir(dr)
    jfile= P+'-dssr.json' #name of the corresponding JSON file, this file contain all characterization output

    with open(jfile, 'r') as f:
        data= json.loads(f.read())
    
    bps_list= pd.json_normalize(data, record_path =['pairs'])
    hbonds_list= pd.json_normalize(data, record_path =['hbonds'])
    stacks_list= pd.json_normalize(data, record_path= 'stacks')
    infos= [bps_list, hbonds_list, stacks_list]
    os.chdir(home)
    return infos

PDB_ID= (input("PDB ID (all in UPPER case):")).upper()
feats= input("type the code of corresponding structure features (0= bp_pairs, 1= hbonds, 2= stacks):")

dr= '' #specify the directory containing the JSON files 
infos= extract_info_from_json(PDB_ID, dr)
df_bps= infos[0]
df_hbonds= infos[1]
df_stacks= infos[2]


#print (df_hbonds)
#print (df_stacks)

if feats==str(0):
    print (df_bps)
    df_bps.to_excel(PDB_ID+'_bps_info.xlsx', index= False)

elif feats==str(1):
    df_hbonds.to_excel(PDB_ID+'_hbonds_info.xlsx', index= False)

elif feats==str(2):
    df_stacks.to_excel(PDB_ID+'_stacks_info.xlsx', index= False)
