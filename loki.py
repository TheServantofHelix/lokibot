#!/usr/bin/python
import praw
import pdb
import re
import os
import time
import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))

# Create the Reddit instance
def bot_login():
    print ("Logging in...")
    reddit = praw.Reddit(client_id=os.environ['CLIENTID'],
                     client_secret=os.environ['CLIENTSECRET'],
                     password=os.environ['PASSWORD'],
                     user_agent='LokiBot v0.1',
                     username='LokiBot')
    print ("Logged in.")
    return reddit

def bot_run(reddit):
    # Get the top 25 values from our subreddit
    print ("Getting 25 submissions")
    subreddit = reddit.subreddit('lokicsstest')
    for submission in subreddit.new(limit=25):
        print(submission.title)
        # If we haven't replied to this post before
        subtime = submission.created_utc
        cyctime = datetime.datetime.time(datetime.datetime.now())
        subtime = subtime.replace(":","\n")
        cyctime = subtime.replace(":","\n")
        print ("Submission Time" + subtime)
        print ("Current Time:" + cyctime)
        #if submission.id not in posts_replied_to:
            #search = submission.title.lower() + submission.selftext.lower()
            #if ('loki' in search and 'rework' in search) or ('loki' in search and 'broken' in search) or ('loki' in search and 'overpowered' in search) or ('loki' in search and 'unfun' in search):
                #reply = open("reply.txt", "r")
                #submission.reply(reply.read())
                #print("Bot replying to : ", submission.title.lower())
    print ("Sleeping for 10 seconds...")
    time.sleep(10)

reddit = bot_login()
while True:
    bot_run(reddit)
