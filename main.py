from Scraper import scrape_memes
from Util.scripts.console import *
from build_video import *
import random 
import shutil

# Set how many videos you want made 
loop_count = 5  # How many videos will be made

print_start("Starting script")

# Set up file paths 
print_start("Set up file paths")
audio_selection = random.randint(1,4)
video_selection = random.randint(1,11)
folder_path = "memes"  # Assuming the folder name is "memes"
output = "Output"

# Make memes folder if it dosn't exists
print_substep("Make memes folder if it dosn't exists") 
if os.path.exists(folder_path):
    print_substep("folder exists")
else:
    # Folder does not exist, so create it
    os.makedirs(folder_path)
    print_substep("Folder created successfully.")

# Make output folder if it dosn't exists 
print_substep("Make output folder if it dosn't exists")
if os.path.exists(output):
    print_substep("folder exists")
else:
    # Folder does not exist, so create it
    os.makedirs(output)
    print_substep("Folder created successfully.")

# Select video and audio paths
print_substep("Selecting video and audio paths") 
audio_path = f"Util/background/background_audios/background_music_{audio_selection}.mp3"
video_path = f"Util/background/background_videos/background_video_{video_selection}.mp4"

# Make memes for meme count
print_start("Make memes for meme count")
for i in range(loop_count): 
    # Scrape memes
    meme_paths, post_title = scrape_memes()

    # Build video
    main(meme_paths, audio_path, video_path, post_title, output)

# Clean up paths
print_substep("Clean up paths")
if os.path.exists(folder_path):
    # Folder exists, so delete it along with its contents
    shutil.rmtree(folder_path)
    print_substep("Folder deleted successfully.")
else:
    print_substep("Folder does not exist.")
