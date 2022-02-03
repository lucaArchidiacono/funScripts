import praw
import auth_parser
    
def getHotPosts(limit: int, conf: auth_parser.Configuration) -> str:
    class Reddit:
        client_id = ""
        client_secret = ""
        password = ""
        user_agent = ""
        username = ""
    
    [reddit] = auth_parser.parse(objects=[Reddit()], conf=conf)

    r = praw.Reddit(
        client_id=reddit.client_id,
        client_secret=reddit.client_secret,
        password=reddit.password,
        user_agent=reddit.user_agent,
        username=reddit.username
    )

    subreddit_list = ["Cringetopia", "dankmemes", "HolUp", "MoldyMemes"]
    subreddits = "+".join([str(x) for x in subreddit_list])

    result = "The 25 hottest posts currently:\n"
    for submission in r.subreddit(subreddits).hot(limit=limit):
        result = result.__add__(f"Title: {submission.title}\n")
        result = result.__add__(f"URL: {submission.url}\n")
    return result