import tweepy
import time

print('This is my twitter bot')
 #authentication api generated from twitter for my app only
CONSUMER_KEY = '4fxFeMqRifa7uEAlnGVcNkbKV'
CONSUMER_SECRET = 'E8Nb3S9dk4ScYTGgo7KGNfGk3ouKrtC6XU3XNbU1Nn4lES3rMn'
ACCESS_KEY = '1232687276095922178-jvyAwqexmOwWmmUGY3MGuf26VDwWd7'
ACCESS_SECRET = 'ZSmssks0aIEtZs3kSrE6Jcwseezc2Suc6wNK298Gaikay'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#storing last seen ID here file

FILE_NAME = 'last_seen_id.txt'

#function for retrive last seen id
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id
# function fo storing last seen id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


# function to provinding reply  to
def reply_to_tweets():
    print('retrieving and replying to tweet...')
    #1232967925272907776 this id of first comment
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    #  We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                            last_seen_id,
                            tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#hey hi' in mention.full_text.lower():
            print('found #hey hi!')
            print('responding back...')
            api.update_status('@'+ mention.user.screen_name +
            '#Hello back to you! and this just test', mention.id)
while True:
    reply_to_tweets()
    time.sleep(15)
