from Scraper import scrape_memes
from Util.scripts.console import *
from build_video import *
import random 
import shutil

# Set how many videos you want made 
loop_count = 10 # How many videos will be made

print_step("Starting script")

# Set up file paths 
print_start("Set up file paths")
folder_path = "memes"  # Assuming the folder name is "memes"
output = "Output"

# Function to get a random file from a directory
def get_random_file(directory, file_extension):
    files = [f for f in os.listdir(directory) if f.endswith(file_extension)]
    if not files:
        raise FileNotFoundError(f"No files with extension {file_extension} found in {directory}")
    return random.choice(files)

# Directories for audio and video files
audio_directory = "Util/background/background_audios"
video_directory = "Util/background/background_videos"

# Select video and audio paths
print_substep("Selecting video and audio paths")
audio_file = get_random_file(audio_directory, ".mp3")
video_file = get_random_file(video_directory, ".mp4")

audio_path = os.path.join(audio_directory, audio_file)
video_path = os.path.join(video_directory, video_file)

print(f"Selected audio file: {audio_path}")
print(f"Selected video file: {video_path}")


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

