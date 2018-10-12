#!/usr/bin/python
import praw
import pdb
import re
import os
import time
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
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
    return reddit


def bot_run(reddit):
    #reddit.login(REDDIT_USERNAME, REDDIT_PASS)
    # Get the top 25 values from our subreddit
    print ("Getting 25 submissions")
    subreddit = reddit.subreddit('lokicsstest')
    for submission in subreddit.new(limit=25):
        # If we haven't replied to this post before
        print ("Checking if we have stored " + submission.title)
        print (getids)
        if submission.id not in getids:
            search = submission.title.lower() + submission.selftext.lower()
            if ('loki' in search and 'rework' in search) or ('loki' in search and 'broken' in search) or ('loki' in search and 'overpowered' in search) or ('loki' in search and 'unfun' in search):
                reddit.redditor('TheServantofHelix').message('Another Post:' + submission.title, 'Link:' + submission.url)
                print("Messaging /u/TheServantofHelix:", submission.title.lower())
                # Store the current id into our list
                print ("Storing " + submission.id + "in the database")
                subid = submission.id
                cur.execute(f"UPDATE posts_replied_to SET ids = (concat(ids,'{subid}'))")
                commit()
    print ("Sleeping for 10 seconds...")
    time.sleep(10)

reddit = bot_login()
print ("Connecting to SQL Database")
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS posts_replied_to (ids text, PRIMARY KEY(ids));")
getids = cur.execute("SELECT ids FROM posts_replied_to;")
getids = cur.fetchall()
if getids is None:
    cur.execute("UPDATE posts_replied_to SET ids = '-Start-'")
commit()
while True:
    bot_run(reddit)
