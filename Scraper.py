from Util.scripts.console import *
from build_video import *
import praw
import requests
import os
import random

def scrape_memes():
    print_step("Scraping memes")

    # Reddit API credentials
    print_substep("Loading reddit API credentials")
    reddit = praw.Reddit(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    )

   # Setting values
    print_substep("Setting values")
    subreddit_list = ['dankmemes','memes','funny', 'Dank']
    save_directory = 'memes'
    used_posts_file = "Util/used_posts.txt"
    num_posts = 2
    num_posts_top = 5
    top_posts = []  # List to store top ten posts
    posts_found = False

    # Randomly select a subreddit
    print_substep("Randomly select a subreddit")
    subreddit_name = random.choice(subreddit_list)
    subreddit = reddit.subreddit(subreddit_name)
    print_substep(f"Scraping from subreddit: {subreddit_name}")
    

    # Create directory if it doesn't exist
    print_substep("Creating directory if it doesn't exist")
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Function to download image from URL
    def download_image(url, filename):
        print_substep("Downloading Meme")
        with open(filename, 'wb') as f:
            f.write(requests.get(url).content)

    # Function to save used post IDs to file
    def save_used_posts(post_ids):
        print_substep("Writing post IDs to used posts file")
        with open(used_posts_file, 'w') as f:  # Open file in write mode to clear previous content
            for post_id in post_ids:
                f.write(post_id + '\n')

    # Function to load used post IDs from file
    def load_used_posts():
        print_substep("Loading post ID from used_post file")
        if not os.path.exists(used_posts_file):
            return set()
        with open(used_posts_file, 'r') as f:
            return set(f.read().splitlines())

    # Load used post IDs
    print_substep("Setting used posts")
    used_posts = load_used_posts()

    # Gathering posts
    posts_gathered = 0
    if not top_posts:  # Only store top ten posts once
        for post in subreddit.top(time_filter='day', limit=None):
            if post.id not in used_posts and ('jpg' in post.url or 'png' in post.url):
                print_substep(f"Checking post for jpg, png")
                posts_found = True
                print_substep(f"Appending post")
                top_posts.append((post.title, post.score))
                posts_gathered += 1
                if posts_gathered >= num_posts_top:
                    print_substep(f"Gathered posts")
                    break 

    # Print top ten post with score in a cleaner formatted box
    print_start("Top Posts")
    display_post_score(top_posts)

    # Scrape memes
    print_start("Scraping memes")
    downloaded_count = 0
    meme_paths = []
    post_title = ""  # Define post_title outside of the if block with a default value
    for post in subreddit.top(time_filter='day', limit=None):  # Iterate over all posts in the subreddit
        if post.id not in used_posts and ('jpg' in post.url or 'png' in post.url):
            print_substep("Checking post")
            posts_found = True

            # Updating post title
            post_title = post.title  # Assign a value to post_title
            print_substep(f"Downloading: {post.title}")

            # Extracting filename from URL
            print_substep("Extracting filename from URL")
            filename = os.path.join(save_directory, os.path.basename(post.url))
            
            # Download image
            download_image(post.url, filename)
            print_substep(f"Saved as: {filename}")
            print_substep("Appending file name to meme paths")
            meme_paths.append(filename)

            # Add post ID to used_posts set
            print_substep("Adding post ID to used_posts set")
            used_posts.add(post.id)
            downloaded_count += 1
            print_progress(downloaded_count, num_posts)

            if downloaded_count >= num_posts:
                break

    # Save used post IDs to file
    save_used_posts(used_posts)

    if posts_found:
        print_finished("Posts found")
    else:
        print_error(f"No suitable posts found in subreddit: {subreddit_name}. Trying another subreddit.")
    
    return meme_paths, post_title

