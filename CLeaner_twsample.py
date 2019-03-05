

from farhad.TwCleaner import Tweets_preprocesiing
import pandas as pd
from IPython.display import HTML
from IPython.display import display
from farhad.Farhadcolor import tcolors,bcolors




if __name__ == "__main__":
    print(tcolors.GREEN)
    
    display(HTML('<h2 style="color:red"><b>input your file:</h2></b>'))
    path_file = str(input('input your file:'))
    df = pd.read_csv(path_file,na_values=['na','?'],encoding='latin-1')
    df.columns= ['label','id','created_at','NO_QUERY','user','text']
    df = df.dropna()
   
    print('coloumns:',df.columns)
    print('info: \n',df.info())
    print('lenght: ',len(df))

    length = int(input('how lenght should be? '))
    from_lenght = int(input('from lenght should be? '))
    df = df[from_lenght:length]
   
    display(HTML("<h2 style='color:red'><b>one of columns:</h2></b> "))
    
    display(HTML('<h2 style="color:red"><b>save file path:</h2></b>'))
    save_file = str(input('save file path:'))
    
    CT = Tweets_preprocesiing()
    data1  = CT.Cleaner(df,target='text',date='created_at')
    data   = CT.Remove_stop_words(data1)
    new_df = CT.save_clean_tweets(df,data,created_at='created_at',name=save_file)
    
    print('\033[0m')