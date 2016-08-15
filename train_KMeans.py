
from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark import SparkContext, SparkConf
from pyspark.mllib.feature import HashingTF, IDF
from pyspark.mllib.feature import Word2Vec


#Initialize spark context to work on RDDs
conf = SparkConf().setAppName('Tweet Classifier')
sc = SparkContext(conf=conf)

# create RDD with preprocessed tweets gathered from online tweet stream
tweets = sc.textFile('tweets_text.txt').map(lambda line: line.split(" "))


# Need to convert text in features. 
# Todo so we need to create TF-IDF for each tweet
# TF-IDF = (Term Frequency) * (Inverse Document Frequency)
hashingTF = HashingTF(20)
tf = hashingTF.transform(tweets)

print 'tf ', tf.take(2)

# cache tf so that it remains in-memory, for faster operations
tf.cache()
idf = IDF(minDocFreq=2).fit(tf)
tfidf = idf.transform(tf)


# We are ready with our feature(TF-IDF) created from tweet text
tweet_model = KMeans.train(tf, 4,
                       maxIterations=10,
                       runs=10,
                       initializationMode='random')
#TODO - implement smart initialization

# save the tweet_model
tweet_model.save(sc, '/home/anshu/Desktop/tweet_classifier/tweet_model')





