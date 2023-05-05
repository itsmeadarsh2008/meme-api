import os
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from sources import get_random_post, get_recent_post, subreddits
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "<b>World</b>"}


@app.get("/random/{subreddit}")
def read_random(subreddit: str):
    try:
        choice = random.choice(subreddits)
        post = get_random_post(choice)
        if subreddit == "any":
            choice = random.choice(subreddits)
            post = get_random_post(choice)
            return {"media": post[1], "caption": post[0], "subreddit": choice}
        else:
            post = get_random_post(subreddit)
            return {"media": post[1], "caption": post[0], "subreddit": subreddit}
    except ValueError as e:
        return {
            "media": None,
            "caption": f"Not Found: Value Error Raised (Available Subreddits: {subreddits})",
            "subreddit": None,
        }


@app.get("/recent/{subreddit}")
def read_recent(subreddit: str):
    try:
        if subreddit == "any":
            choice = random.choice(subreddits)
            post = get_recent_post(choice)
            return {"media": post[1], "caption": post[0], "subreddit": choice}
        else:
            post = get_recent_post(subreddit)
            return {"media": post[1], "caption": post[0], "subreddit": subreddit}
    except ValueError as e:
        return {
            "media": None,
            "caption": f"Not Found: Value Error Raised (Available Subreddits: {subreddits})",
            "subreddit": None,
        }

#END
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Memes API by Adarsh",
        version=os.system('git describe --abbrev=7 --always  --long --match'),
        description="A simple api to steal memes from Reddit.",
        routes=app.routes
    )
    # openapi_schema["info"]["x-logo"] = {
    #     "url": "<img_path>"
    # }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi