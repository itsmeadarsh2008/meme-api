<h1 align="center">MEMES-API</h1>
<p align="center">
<img src="https://img.shields.io/github/repo-size/itsmeadarsh2008/meme-api?color=pink&style=for-the-badge">
<img src="https://img.shields.io/github/issues/itsmeadarsh2008/meme-api?style=for-the-badge">
</p>

A simple API made with Python and FastAPI to fetch memes from Reddit. 

## Endpoints
| NOTE: VERCEL CRASHES SOMETIMES     |
|------------------------------------|
| https://meme-api-ashy.vercel.app   |
| https://meme-api-ws81.onrender.com |
>RECOMMENDED: Please use CURL or other HTTP clients that don't replace commas (,) with %2C. 

## Usage

### Endpoints

- `/random/{subreddit}`: Get a random meme from a subreddit.
- `/recent/{subreddit}`: Get a recent meme from a subreddit.
- `/docs`: Swagger UI documentation
- `/redoc`: ReDocly Documentation

### Query Parameters

- `subreddit` (Require): Name of the subreddit to fetch the meme from. Use `any` to fetch from any random subreddit. Multiple subreddits can be provided by separating them with commas (`,`).
- `count` (optional): Number of memes to fetch. Default is `1`.

### Example Requests

Get a random meme from any subreddit:

```
curl https://meme-api-ws81.onrender.com/random
```

Get a random meme from `dankmemes` subreddit:

```
curl https://meme-api-ws81.onrender.com/random/dankmemes
```

Get 3 recent memes from `memes` subreddit:

```
curl https://meme-api-ws81.onrender.com/recent/memes?count=3
```

Get 5 recent memes from `dankmemes` and `funny` subreddits:

```
curl https://meme-api-ws81.onrender.com/recent/dankmemes,funny?count=5
```

## License

This project is licensed under the terms of the MIT license.