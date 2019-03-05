import warnings
warnings.filterwarnings('ignore')
from getiing_news import __info_getnews__
from getiing_news import CENT_news_extract, Yahoo_finacial_news_extract, Nytimes_news_extract, marketwatch_news_extract
import pandas as pd
from farhad.Farhadcolor import bcolors,tcolors
print(tcolors.BLUE)

""" Tesla """
words= ['tesla']
Yahoo = Yahoo_finacial_news_extract(words=words)
Yahoo.Yahoo_finacial_search_topic()
Yahoo.Yahoo_finacial_search_subscript()
df = Yahoo.Yahoo_save_file(savename='/Users/apple/Documents/Programming/python/Project/Collected/Collected_News/Tesla/Tesla_Yahoo_finacial_new.csv')
df.head()

print(tcolors.GREEN)
words= ["tesla"]
CNET = CENT_news_extract(words)
CNET.CENT_news_topics()
CNET.CENT_news_search_subscript()
df = CNET.CENT_save('/Users/apple/Documents/Programming/python/Project/Collected/Collected_News/Tesla/Tesla_CENT_new.csv')
df.head()

print(tcolors.BLUE)
words= ["tesla"]
Nytimes = Nytimes_news_extract(words)
Nytimes.Nytimes_news_topics()
Nytimes.Nytimes_news_search_subscript()
df_Nytimes = Nytimes.Nytimes_save('/Users/apple/Documents/Programming/python/Project/Collected/Collected_News/Tesla/Tesla_Nytimes_new.csv')
df_Nytimes.head()

print(tcolors.GREEN)
words= ["Tesla"]
marketwatchT = marketwatch_news_extract(words)
marketwatchT.marketwatch_news_topics()
marketwatchT.marketwatch_news_search_subscript()
df_marketwatchT = marketwatchT.marketwatch_save(nameSave="/Users/apple/Documents/Programming/python/Project/Collected/Collected_News/Tesla/Tesla_marketwatch_new.csv")
df_marketwatchT.head()


""" Apple """

print(tcolors.BLUE)
words= ['Apple']
Yahoo = Yahoo_finacial_news_extract(words=words)
Yahoo.Yahoo_finacial_search_topic()
Yahoo.Yahoo_finacial_search_subscript()
df = Yahoo.Yahoo_save_file('/Users/apple/Documents/Programming/python/Project/Collected/Collected_News/Apple/Apple_Yahoo_finacial_new.csv')
df.head()

print(tcolors.GREEN)
words= ["Apple"]
CNET = CENT_news_extract(words)
CNET.CENT_news_topics()
CNET.CENT_news_search_subscript()
df = CNET.CENT_save('/Users/apple/Documents/Programming/python/Project/Collected/Collected_News/Apple/Apple_CENT_new.csv')
df.head()

print(tcolors.BLUE)
words= ["Apple"]
Nytimes = Nytimes_news_extract(words)
Nytimes.Nytimes_news_topics()
Nytimes.Nytimes_news_search_subscript()
df_Nytimes = Nytimes.Nytimes_save('/Users/apple/Documents/Programming/python/Project/Collected/Collected_News/Apple/Apple_Nytimes_new.csv')
df_Nytimes.head()

print(tcolors.GREEN)
words= ["Apple"]
marketwatch = marketwatch_news_extract(words)
marketwatch.marketwatch_news_topics()
marketwatch.marketwatch_news_search_subscript()
df_marketwatch = marketwatch.marketwatch_save(nameSave="/Users/apple/Documents/Programming/python/Project/Collected/Collected_News/Apple/Apple_marketwatch_new.csv")
df_marketwatch.head()

print('\033[0m')