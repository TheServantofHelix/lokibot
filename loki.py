#!/usr/bin/python
import praw
import pdb
import re
import os
import time
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
    #reddit.login(REDDIT_USERNAME, REDDIT_PASS)
    # Have we run this code before? If not, create an empty list
    if not os.path.isfile(dir_path + "\posts_replied_to.txt"):
        posts_replied_to = []
    # If we have run the code before, load the list of posts we have replied to
    else:
        # Read the file into a list and remove any empty values
        with open(dir_path + "\posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))
    # Get the top 25 values from our subreddit
    print ("Getting 25 submissions")
    subreddit = reddit.subreddit('smite')
    for submission in subreddit.new(limit=25):
        print(submission.title)
        # If we haven't replied to this post before
        print ("Checking if we have replied to " + submission.title)
        if submission.id not in posts_replied_to:
            search = submission.title.lower() + submission.selftext.lower()
            if ('loki' in search and 'rework' in search) or ('loki' in search and 'broken' in search) or ('loki' in search and 'overpowered' in search) or ('loki' in search and 'unfun' in search):
                reply = open("reply.txt", "r")
                submission.reply(reply.read())
                print("Bot replying to : ", submission.title.lower())
                # Store the current id into our list
                print ("Storing " + submission.id + " in posts_replied_to.txt")
                posts_replied_to.append(submission.id)
                print (posts_replied_to)
    print ("Sleeping for 10 seconds...")
    time.sleep(10)

reddit = bot_login()
while True:
    bot_run(reddit)
