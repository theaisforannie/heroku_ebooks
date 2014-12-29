'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'y1m0Nb9aPMGsIHXHOfA3eKlXb'
MY_CONSUMER_SECRET = 'gc3F5GMJU7YKtPLeEnaux3sqMbB5vo8eVhY1dXUqNJjxpaRt5N'
MY_ACCESS_TOKEN_KEY = '2950669142-moCwV9SrVqjGbIyNopoLICSrI6CnnkqXO4IFtAx'
MY_ACCESS_TOKEN_SECRET = 'sQivwRvMAq0cLdpjDC0MwZxHW93eTe5QklZEsk4hgVxH6'

SOURCE_ACCOUNTS = ["anyharder"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 4 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "ann_iebooks" #The name of the account you're tweeting to.
