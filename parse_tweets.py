import json
import pandas as pd
import re
import sys

allText = []

raw_tweets = sys.argv[1] # input
clean_tweets = sys.argv[2] # output
with open(raw_tweets) as tweets:
   '''Filter all english tweets 
   also remove the links.
   '''
   for line in tweets:
      jsonLine = json.loads(line)
      try:
         if jsonLine['lang'] == 'en':
            filteredLinks = re.sub(r"http\S+", "", jsonLine['text'])
            filteredLinks = re.sub(r"[\n\t\r]", " ", filteredLinks)
            filteredLinks = re.sub(r'[^a-zA-Z0-9-_*.@# ]', '', filteredLinks)
            filteredLinks = re.sub(r'RT', '', filteredLinks)
            allText.append(filteredLinks)
      except:
         pass
      

if __name__ == '__main__':
      with open(clean_tweets, 'a') as f:
         for line in allText:
            f.write(line+"\n")
      '''
      for line in allText:
         print(line)
      '''
