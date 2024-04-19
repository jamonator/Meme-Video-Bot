# Meme Video Builder

This project automates the creation of meme videos by scraping memes from selected subreddits, combining them with background music and videos, and generating a final video output.

## Features

- Scrapes memes from Reddit using PRAW API.
- Combines memes with background audio and video to create meme videos.
- Outputs the generated videos in YouTube Shorts format.

## Installation

1. Clone the repository:
2. Follow this [tutorial](https://youtu.be/4-ogv3ZU6dg) to get your Reddit API keys
3. Replace the info on lines 13-16 with your info 

   ```bash
   git clone https://github.com/jamonator/Meme-Video-Bot.git

## Install dependencies:

```python
pip install -r requirements.txt
```

## Usage

- Add your reddit info to line 13 - 16 
- Set the number of videos you want to generate in the loop_count variable in main.py.
- The generated videos will be available in the Output folder

### Run the script:

```python
python main.py
```

## Main dependencies

- Python 3.x
- praw
- moviepy
- opencv-python

## Configuration

- Adjust subreddit selection, number of posts to scrape, and other settings in the scrape_memes() function in Scraper.py.
- Customize background audio and video selection in main.py.

## Example
https://github.com/jamonator/Meme-Video-Bot/assets/83436730/b86c6ad4-fbae-4668-8691-c4a850391c0c

### Notes from the creator
- This is very bad code
- This much like my other projects is not made with the intention of easy use or works first-time type stuff, it worked on my end so I uploaded it 
- Sorry if it don't work
- Good luck getting it working for yourself
- If you want to please make a better version of my project and show me, that would be cool :)
- Any of this code can be used I don't care
