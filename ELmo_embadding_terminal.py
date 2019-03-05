
import numpy as np
import pandas as pd
from tqdm import tqdm
from  ELmo import ELMo_google_model
import re
import logging
logging.getLogger('tensorflow').disabled = True #OPTIONAL - to disable outputs from Tensorflow

def read_file():
    print('/*file should have  the name cloumn is text')
    print('/*put file that you want to embadding:')
    address = str(input())
    df_data = pd.read_csv(address, na_values=['na','?'])
    df_data.dropna()
    try:
        df_data['text'] = df_data['text'].apply(lambda x: re.sub('-PRON- ','',str(x)))
    except:
        print("this file doesn't have text_column")
        print(df_data.columns)
        target= str(input())
        df_data['text'] = df_data[target].apply(lambda x: re.sub('-PRON- ','',str(x)))
    print('/*length of dataframe:',len(df_data))    
    print('/*how many rows do you want embadding do:')
    number = int(input())
    df = df_data[:number]
    return df 

""" ELMo """
if __name__ == "__main__":
    print('\033[94m ')

    df = read_file()
     
    print('\033[93m')
    dimension = int(input('** length of dimension:'))
    namefile = str(input('** file_save:'))

    
    Elmo = ELMo_google_model(df,name='text',dimension=dimension)
    x= Elmo.ELMo_Embadding()
    Elmo.Save_ELMo(namefile=namefile)

    print('\033[0m')