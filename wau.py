import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("<the name of the reddot>")

for submission in subreddit.hot(limit=4000):
    if "keywords " in submission.title:
        print("Title: ", submission.title)
        print("Text: ", submission.selftext)
        print("---------------------------------\n")