# tweet_clustering

This application classify live tweets to appropriate cluster, so that we can get an idea about the current trend on twitter.

###How to Run
(1) First gather the data using gather_tweets.py
   
   $python3 gahter_tweets.py -c "consumer-key" -s "consumer-secret-key" -a "access-token" -S "access-token-secret"
   
     We need to register to twitter app for api aceess. link - https://apps.twitter.com/. 
   
     Please follow the link to have one - http://www.slickremix.com/docs/how-to-get-api-keys-and-tokens-for-twitter/
   
     You need to specify your own <consumer-key>, <consumer-secret-key>, <access-token>, <access-token-secret> to get api access.
   
     Gahterd tweets will saved to tweets.json.
   
   
