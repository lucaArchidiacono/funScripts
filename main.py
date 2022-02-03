from auth_parser import Configuration
import reddit_meme_crawler

conf = Configuration("authentication.txt", "=")

hottest_posts = reddit_meme_crawler.getHotPosts(25, conf=conf)

print(hottest_posts)