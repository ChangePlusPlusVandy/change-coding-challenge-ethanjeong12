import json
import requests
import oauth2
import re
import random
import tweepy
from .config   import *
from .forms    import UserInput

from django.views     import View
from django.http      import (
JsonResponse,
HttpResponse,
HttpResponseRedirect
)
from django.shortcuts import render

# global variable
count = 0
correct = 0

# generating a random tweet
def get_random_tweet():
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=ACCESS_TOKEN, secret=ACCESS_SECRET)
    client = oauth2.Client(consumer, token)
    
    # api call for kanye
    screen_name = "kanyewest"
    count = 3200 
    include_rts = "False"
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}&include_rts={}'.format(screen_name, count, include_rts)
    response, data = client.request(url)
    decoded_response = json.loads(data.decode('utf-8'))
    
    tweet_list_kanye=[]
    for tweet in decoded_response:
        filtered = re.sub(r'https:.*$', "", tweet['text'])
        filtered = re.sub(r'@.*$', "", filtered)

        if filtered == '':  # skipping the unfiltered tweets
            continue
        if tweet['retweeted'] == True:  # removing all the retweets
            continue
        else:
            tweet_list_kanye.append(filtered)      
    kanye_dict = {'Kanye': tweet_list_kanye}

    # api call for elonmusk 
    screen_name = "elonmusk"
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={}&count={}&include_rts={}'.format(screen_name, count, include_rts)
    response, data = client.request(url)
    decoded_response = json.loads(data.decode('utf-8'))

    tweet_list_elon=[]
    for tweet in decoded_response:
        filtered = re.sub(r'https:.*$', "", tweet['text'])
        filtered = re.sub(r'@.*$', "", filtered)

        if filtered == '':  # skipping the unfiltered tweets
            continue
        if tweet['retweeted'] == True:  # removing all the retweets
            continue
        else:
            tweet_list_elon.append(filtered)
    elon_dict = {'Elon': tweet_list_elon}

    # merging two dataframes
    kanye_dict.update(elon_dict)
    merged = list(kanye_dict.items())
    
    return merged

def determineAnswer(random_tweet):
    # Authentication
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    # get the user name for a given random tweet
    answer_li = []
    max_tweets = 50
    search_result = [status for status in tweepy.Cursor(api.search, q=random_tweet).items(max_tweets)]
    #search_result = api.search(q=random_tweet.strip(), count=100)
    for i in range(len(search_result)):
        json_str = json.dumps(search_result[i]._json)
        final_str = json.loads(json_str)
        try:
            answer_li.append(final_str['entities']['user_mentions'][0]['screen_name'])
        except:
            continue
    return answer_li 

def index(request):
    global correct
    global count

    try: 
        merged = get_random_tweet()

        # choosing a random to render
        filtered_tweets = random.choice(merged)
        random_tweet = random.choice(filtered_tweets[1])
       
        # figuring out the answer
        answer_list = determineAnswer(random_tweet)
        if 'kanyewest' in answer_list:
            answer = 'Kanye'
        elif 'elonmusk' in answer_list:
            answer = 'Elon'

        if request.method == 'POST':
            user_input = request.POST['description']
            if answer == user_input.strip():
                count += 1
                correct += 1
                return HttpResponseRedirect("http://127.0.0.1:8000/tweets/display?msg=CORRECT")
            else:
                count += 1
                return HttpResponseRedirect('http://127.0.0.1:8000/tweets/display?msg=INCORRECT')

        if request.method == 'GET':
            result = {
                'Random_Tweet': random_tweet,
            }
            return render(request, 'index.html', result)
    except:
        return render(request, 'trouble.html')

def result(request):
    if count == 0:
        stats = 0
    else:
        stats= (correct/count)*100
    result = {
        'total_count': count,
        'correct_count': correct,
        'Statistics': stats 
    }

    return render(request, 'result.html', result)
