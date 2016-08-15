from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark import SparkContext, SparkConf
from pyspark.mllib.feature import HashingTF, IDF


#Initialize spark context to work on RDDs
conf = SparkConf().setAppName('Tweet Classifier')
sc = SparkContext(conf=conf)
test_data = sc.textFile('tweet_test_text.json').map(lambda line: line.split(" "))
print 'test_data', test_data.take(4)
tweet_model = KMeansModel.load(sc, '/home/anshu/Desktop/tweet_classifier/tweet_model')

hashingTF = HashingTF(20)
tf = hashingTF.transform(test_data)
idf = IDF(minDocFreq=2).fit(tf)
tfidf = idf.transform(tf)

#print 'tfidf : ', tf.take(4)

#"RT @TimesNow We are calling upon India to help us. I am very grateful to PM for raising the issue of Balochistan Ahmar Mustikhan #IndiaFo"
print(len(tweet_model.clusterCenters))
print('value of k ', tweet_model.k)

print 'cluster 1 points ', tweet_model.centers[1]
print 'cluster 2 points ', tweet_model.centers[2]
print 'cluster 3 points ', tweet_model.centers[3]

#print 'feature ', tfidf.take(3)

predictedClusters = tf.map(lambda feature: tweet_model.predict(feature)).collect()

print 'predicted lables ', predictedClusters
        
#labels = tweet_model.predict(tfidf).collect()
#print('predicted Labels ', labels)
