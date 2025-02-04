# Jozetova igračka
This discord bot was made for fun and to learn how to use discord.py and openai api. As well as containerization with docker.
## Features
- Leaderboard of **longest** time spent in voice channel while being muted or deafened
- Leaderboard of **cumulative** time spent in voice channel while being muted or deafened
- Speaks in voice chat using openai's gpt-3, when the user, that originally ran the command, sends a message in the chat
- Plays sound quips

# Docker
## Maintainers
This image is maintained by:
- [JozeJan](https://github.com/JozeJan)
- [Privatech](https://github.com/Privatech38)

## How to use this image
**Start a jozetova-igracka instance**

Start without mounting the data to a specific location
```
docker run --name some-jozetova-igracka -e DISCORD-TOKEN=mydiscordtoken OPENAI_API_KEY=myopeaniapikey -d jozejan/jozetova-igracka
```

or with mounting the data to a specific location
```
docker run --name some-jozetova-igracka -e DISCORD-TOKEN=mydiscordtoken OPENAI_API_KEY=myopeaniapikey -v /path/to/data:/data -d jozejan/jozetova-igracka
```

**Environment Variables**

This image uses the following environment variables:
### `DISCORD_TOKEN`
This environment variable is required. 
It sets the discord bot's token used by the application.

### `OPENAI_API_KEY`
This environment variable is required.
It sets the openai api key used by the application.