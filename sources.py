import requests
import random


endpoint = "https://www.reddit.com"
headers = {"User-Agent": "my-app/0.0.1"}
def get_recent_post(subreddit):
    url = f"{endpoint}/r/{subreddit}/new.json"
    response = requests.get(url, headers=headers)
    data = response.json()
    top_post = data["data"]["children"][0]["data"]
    return (top_post["title"], top_post["url"])


def get_random_post(subreddit):
    url = f"{endpoint}/r/{subreddit}/.json"
    response = requests.get(url, headers=headers)
    data = response.json()
    posts = data["data"]["children"]
    random_post = random.choice(posts)["data"]
    return (random_post["title"], random_post["url"])


subreddits = ["any","dankmemes", "memes", "funny","outofcontextcomics"]