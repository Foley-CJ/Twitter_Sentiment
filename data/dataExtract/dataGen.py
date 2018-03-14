import urllib2
import getpass
from dataGenConstants import companies, finaceMasterUrl
import tweepy

#twitterApiKey =                   #getpass.getpass(prompt="Twitter api key: ")
finaceApiKey = "JB6GKB3YZ53KGCX3" #getpass.getpass(prompt="Finance api key: ")




def finaceData(financeApiKey):
	for company in companies:
		company['finaceApiKey'] = finaceApiKey
		curFinanceUrl = finaceMasterUrl.format(**company)
		print curFinanceUrl
		finResponse = urllib2.urlopen(curFinanceUrl)
		with open('raw/finance/'+company['companyName']+'_finance.dat','w') as f:
			for row in finResponse:
				f.write(row)



# Consumer keys and access tokens, used for OAuth
consumer_key = "Rriom1HaYquDdAog0B5t2HlAu"  #getpass.getpass(prompt="Twitter consumer key: ")
consumer_secret = "3NWlZpnhFvpxxxeu2t941rwWaM5C00V3vMKuMclwXcnQKqCCVr" #getpass.getpass(prompt="Twitter consumer secret key: ")
access_token = "810993381098725376-jBu98MU8CKMSpzZGMsNngGkHIhjKtC4" #getpass.getpass(prompt="Twitter access key: ")
access_token_secret = "bbkR09mbSt7kKYw7hG1RyLT0acKtd31AuKD4CkzdYX2Fm" #getpass.getpass(prompt="Twitter access secret key: ")




def twitterData(consumer_key,consumer_secret,access_token,access_token_secret):
	# OAuth process, using the keys and tokens
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	# Creation of the actual interface, using authentication
	api = tweepy.API(auth)

	for company in companies:
		handle = company['twitterSymbol']
		if handle == 'not_applicable':
			continue
		print handle
		zed = 0
		with open('raw/twitter/'+company['companyName']+'_twitter.dat','w') as f:
			for page_number in range(0,1):

				for status in tweepy.Cursor(api.user_timeline, screen_name=handle,page=page_number).items():
					#print status._json
					print zed
					zed = zed + 1

					if zed >= 3:
						break
					data = ','.join(['"'+str(status._json[x].encode('ascii','ignore')).replace('/n',' ')+'"' for x in ['text', 'created_at']])
					print data
					#f.write(data)





twitterData(consumer_key,consumer_secret,access_token,access_token_secret)




#in_reply_to_user_id_str


# def twitterData(consumer_key, consumer_secret, access_token, access_token_secret):
# 	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# 	auth.set_access_token(access_token, access_token_secret)

# 	api = tweepy.API(auth)

# 	#public_tweets = api.home_timeline()
# 	public_tweets = api.user_timeline('@TheCJFoley')
# 	for tweet in public_tweets:
# 	    print tweet.text.encode('ascii','ignore')

#twitterData(consumer_key, consumer_secret, access_token, access_token_secret)



# if __name__ ='main':
# 	#financeData(financeApiKey)
# 	twitterData()

