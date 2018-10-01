#!/usr/bin/python
import praw
import pdb
import re
import os
import time
import psycopg2
dir_path = os.path.dirname(os.path.realpath(__file__))
DATABASE_URL = os.environ['DATABASE_URL']

# Create the Reddit instance
def bot_login():
    print ("Logging in...")
    reddit = praw.Reddit(client_id=os.environ['CLIENTID'],
                     client_secret=os.environ['CLIENTSECRET'],
                     password=os.environ['PASSWORD'],
                     user_agent='LokiBot v0.1',
                     username='LokiBot')
    print ("Logged in.")
    print ("Creating SQL Database")
    table = (
    CREATE DATABASE lokibot;
    CREATE TABLE posts_replied_to (
    ids ARRAY NOT NULL )
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cur = conn.cursor()
    cur.execute(table)
    return reddit


def bot_run(reddit):
    #reddit.login(REDDIT_USERNAME, REDDIT_PASS)
    # Get the top 25 values from our subreddit
    print ("Getting 25 submissions")
    subreddit = reddit.subreddit('lokicsstest')
    for submission in subreddit.new(limit=25):
        print(submission.title)
        # If we haven't replied to this post before
        print ("Checking if we have replied to " + submission.title)
        getids = SELECT ids FROM posts_replied_to;
        if submission.id not in getids:
            search = submission.title.lower() + submission.selftext.lower()
            if ('loki' in search and 'rework' in search) or ('loki' in search and 'broken' in search) or ('loki' in search and 'overpowered' in search) or ('loki' in search and 'unfun' in search):
                reply = open("reply.txt", "r")
                submission.reply(reply.read())
                print("Bot replying to : ", submission.title.lower())
                # Store the current id into our list
                print ("Storing " + submission.id + " database")
                INSERT INTO posts_replied_to(ids) VALUES (submission.id)
    print ("Sleeping for 10 seconds...")
    time.sleep(10)

reddit = bot_login()
while True:
    bot_run(reddit)
