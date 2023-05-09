import os
from fastapi import FastAPI, Response
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from sources import get_random_post, get_recent_post, subreddits
import random
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"detail": f"Go to /redoc or /docs"}

@app.get("/random/{subreddit}")
def read_random(subreddit: str = "any", count: int = 1):
    try:
        if subreddit == "any":
            subreddits_list = subreddits
        else:
            subreddits_list = subreddit.split(",")
        memes = []
        for _ in range(count):
            choice = random.choice(subreddits_list)
            post = get_random_post(choice)
            memes.append({"media": post[1], "caption": post[0], "subreddit": choice})
        response_data = memes
    except ValueError:
        response_data = {"detail": f"Not Found: Available Subreddits: {', '.join(subreddits)}"}
    response_body = json.dumps(response_data)
    media_type = "application/json"
    return Response(content=response_body, media_type=media_type)

@app.get("/recent/{subreddit}")
def read_recent(subreddit: str = "any", count: int = 1):
    try:
        if subreddit == "any":
            subreddits_list = subreddits
        else:
            subreddits_list = subreddit.split(",")
        memes = []
        for _ in range(count):
            choice = random.choice(subreddits_list)
            post = get_recent_post(choice)
            memes.append({"media": post[1], "caption": post[0], "subreddit": choice})
        response_data = memes
    except ValueError:
        response_data = {"detail": f"Not Found: Available Subreddits: {', '.join(subreddits)}"}
    response_body = json.dumps(response_data)
    media_type = "application/json"
    return Response(content=response_body, media_type=media_type)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Memes API by Adarsh",
        version=os.popen('git describe --abbrev=7 --always --match "*"').read().strip(),
        description=f"A simple API made with Python and FastAPI to fetch memes from Reddit. Available subreddits are {', '.join(subreddits)}. 'any' means randomly selected subreddit.",
        routes=app.routes
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://i.ibb.co/JBCdS67/Our-climate-is-changing-Why-aren-t-we-MEMES-API.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
