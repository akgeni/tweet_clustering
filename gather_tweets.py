from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

from parse_arguments import parseArguments

# Get credentials from command line
credentials = parseArguments()
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret
consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret 

fileName = sys.argv[1] + '.json'
class StdOutListener(StreamListener):
   '''Redirects tweets from stream to stdout
   '''
   def on_data(self, data):
      try:
         with open(fileName, 'a') as f:
            f.write(data)
            return True
      except BaseException as exp:
         print('Error on_data' % (str(exp)))
      return True

   def on_error(self, status):
      print(status)


if __name__ == "__main__":
   listener = StdOutListener()
   auth = OAuthHandler(consumer_key, consumer_secret)
   auth.set_access_token(access_token, access_token_secret)
   stream = Stream(auth, listener)

   stream.filter(track=['India', 'rio', 'isis', 'vmware', 'Hillary Clinton', 'Modi'])


