import praw
from time import sleep

r = praw.Reddit(client_id='SASQjg-CXDy8-g',
                client_secret='JdnLCd1DwsISCtb_yOASwoCqXG8',
                password='jacksucks420',
                username='WednesdayBot_1',
                user_agent='Nice.')
print("logged in")


cache = []

Wednesday = set()
for i in range(0,10):
    subreddit = r.subreddit('BackToSchoolDeals')
    comments = subreddit.comments(limit = 20)
    for comment in comments:
        body = comment.body.lower()
        if ("monday" in body) and (comment.id not in cache):
            comment.reply("Not Good")
            cache.append(comment.id)
            print("Monday = Done")
    subreddit = r.subreddit('BackToSchoolDeals')
    comments = subreddit.comments(limit = 20)
    for comment in comments:
        body = comment.body.lower()
        if ("tuesday" in body) and (comment.id not in cache):
            comment.reply("Okay")
            cache.append(comment.id)
            print("Tuesday = Done")
    subreddit = r.subreddit('BackToSchoolDeals')
    comments = subreddit.comments(limit = 20)
    for comment in comments:
        body = comment.body.lower()
        if ("wednesday" in body) and (comment.id not in cache):
            comment.reply("My Dudes")
            cache.append(comment.id)
            print("Wednesday = Done")
    subreddit = r.subreddit('BackToSchoolDeals')
    comments = subreddit.comments(limit = 20)
    for comment in comments:
        body = comment.body.lower()
        if ("thursday" in body) and (comment.id not in cache):
            comment.reply("Mediocre")
            cache.append(comment.id)
            print("Thursday = Done")
    subreddit = r.subreddit('BackToSchoolDeals')
    comments = subreddit.comments(limit = 20)
    for comment in comments:
        body = comment.body.lower()
        if ("friday" in body) and (comment.id not in cache):
            comment.reply("Great")
            cache.append(comment.id)
            print("Friday = Done")
    subreddit = r.subreddit('BackToSchoolDeals')
    comments = subreddit.comments(limit = 20)
    for comment in comments:
        body = comment.body.lower()
        if ("saturday" in body) and (comment.id not in cache):
            comment.reply("The Best")
            cache.append(comment.id)
            print("Saturday = Done")
    subreddit = r.subreddit('BackToSchoolDeals')
    comments = subreddit.comments(limit = 20)
    for comment in comments:
        body = comment.body.lower()
        if ("sunday" in body) and (comment.id not in cache):
            comment.reply("Bad")
            cache.append(comment.id)
            print("Sunday = Done")
    sleep(25)
        
