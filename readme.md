# Meme Video Builder

This project automates the creation of meme videos by scraping memes from selected subreddits, combining them with background music and videos, and generating a final video output.

## Features

- Scrapes memes from Reddit using PRAW API.
- Combines memes with background audio and video to create meme videos.
- Outputs the generated videos in YouTube Shorts format.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jamonator/Meme-Video-Bot

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

## Dependencies

- Python 3.x
- praw
- moviepy
- opencv-python

## Configuration

- Adjust subreddit selection, number of posts to scrape, and other settings in the scrape_memes() function in Scraper.py.
- Customize background audio and video selection in main.py.
- Make sure to replace `your-username` with your GitHub username in the installation section. You can further expand or customize this `README.md` based  on your project's requirements.