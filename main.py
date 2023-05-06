import os
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from sources import get_random_post, get_recent_post, subreddits
import random

app = FastAPI()

@app.get("/")
def read_root():
    return {"detail": f"Go To /redoc or /docs"}


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
        description=f"A simple API made with Python and FastAPI to steal memes from Reddit. Available subreddits are {', '.join(subreddits)}. 'any' means randomly selected subreddit.",
        routes=app.routes
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://i.ibb.co/JBCdS67/Our-climate-is-changing-Why-aren-t-we-MEMES-API.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi