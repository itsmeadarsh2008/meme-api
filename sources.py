import requests
import random

endpoint = "https://www.reddit.com"
headers = {"User-Agent": "my-app/0.0.1"}

VALID_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".mp4", ".webm", ".gifv"]

def get_recent_post(subreddit, return_only_with_extension=False):
    url = f"{endpoint}/r/{subreddit}/new.json"
    response = requests.get(url, headers=headers)
    data = response.json()
    top_post = data["data"]["children"][0]["data"]
    post_url = top_post["url"]
    if return_only_with_extension:
        if not any(post_url.endswith(ext) for ext in VALID_EXTENSIONS):
            return None
    return (top_post["title"], post_url)


def get_random_post(subreddit, return_only_with_extension=False):
    url = f"{endpoint}/r/{subreddit}/.json"
    response = requests.get(url, headers=headers)
    data = response.json()
    posts = data["data"]["children"]
    random_post = random.choice(posts)["data"]
    post_url = random_post["url"]
    if return_only_with_extension:
        if not any(post_url.endswith(ext) for ext in VALID_EXTENSIONS):
            return None
    return (random_post["title"], post_url)


subreddits = [
    "any",
    "dankmemes",
    "memes", 
    "funny",
    "outofcontextcomics",
    "wholesomememes",
    "me_irl"
]
