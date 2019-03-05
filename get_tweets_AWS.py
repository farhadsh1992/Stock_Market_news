import datetime
from farhad.Get_tweets_awesome import get_twitter 
import pandas as pd
from pendulum import now
from farhad.Farhadcolor import tcolors
from farhad.Farhadcolor import tcolors,bcolors
print(tcolors.GREEN)

query = str(input('put quesry words:'))
namesave = '/Users/apple/Documents/Programming/python/Project/Collected/Collected_Tweets/{}{}{}collection_tweets_about_{}.csv'.format(now().year,now().month,now().day,query)
item = 2000

try:
    twitter = get_twitter(query,item,namesave)
    twitter.authenticate_twitter_app()
    df = twitter.get_by_query_until()
    print(bcolors.WHITE)
    print('Address that file_save:', namesave)
    time1 = df.sort_values('created_at')['created_at'][0]
    time2 = df.sort_values('created_at')['created_at'][len(df)-1]
    print('From:',time1)
    print('To:',time2)
    print(bcolors.ENDC)
except:
    print(tcolors.RED+"Can't download_ check the file"+tcolors.ENDC)


    