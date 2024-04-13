from Util.scripts.scruber import scrub_text
from Util.scripts.console import *
import cv2
from moviepy.editor import *
import os

def convert_video_to_shorts_format(video_path, audio_path, output_path):
    print_start("Converting video to YouTube Shorts format")

    # Use moviepy to resize the video to YouTube Shorts format
    print_substep("Setting video and audio")
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # Calculate new dimensions
    print_substep("Calculating new dimensions")
    target_height = 1920
    target_width = 1080
    video_ratio = video.size[0] / video.size[1]
    target_ratio = target_width / target_height

    # Crop horizontally
    if video_ratio > target_ratio: 
        print_substep("Crop horizontally")
        new_width = int(video.size[1] * target_ratio)
        x_offset = (video.size[0] - new_width) / 2
        cropped_video = video.crop(x1=x_offset, x2=video.size[0] - x_offset)
    
    # Crop vertically
    else:
        print_substep("Crop vertically")
        new_height = int(video.size[0] / target_ratio)
        y_offset = (video.size[1] - new_height) / 2
        cropped_video = video.crop(y1=y_offset, y2=video.size[1] - y_offset)

    # Resize the video to YouTube Shorts format (1080x1920)
    print_substep("Resizing the video")
    resized_video = cropped_video.resize((target_width, target_height))

    # Set the duration of the video to match the duration of the audio
    print_substep("Setting the duration")
    resized_video = resized_video.set_duration(audio.duration)

    # Set the audio of the resized video to the audio clip
    print_substep("Setting the audio")
    resized_video = resized_video.set_audio(audio)

    # Write the resized video with audio to the output file
    print_substep("Writting the resized video")
    resized_video.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile='temp-audio.m4a', remove_temp=True, fps=24)

def add_images_to_video(video_path, top_image_path, bottom_image_path, output_path, padding=50):
    print_start("Add images to the video")

    # Setting the video path
    print_substep("Setting video path")
    video = VideoFileClip(video_path)
    fps = video.fps
    frame_width, frame_height = video.size

    # Load images
    print_substep("Loading images")
    top_image = ImageClip(top_image_path)
    bottom_image = ImageClip(bottom_image_path)

    # Define the desired height for the images
    print_substep("Defining the desired height")
    image_height = frame_height // 3  # Adjust as needed

    # Resize images while maintaining aspect ratio
    print_substep("Resize images while maintaining aspect ratio")
    top_image = top_image.resize(height=image_height)
    bottom_image = bottom_image.resize(height=image_height)

    # Calculate the center position of the frame
    print_substep("Calculating the center position of the frame")
    center_x = frame_width // 2
    center_y = frame_height // 2

    # Calculate the positions to center images horizontally and vertically
    print_substep("Calculating the positions to center images horizontally and vertically")
    top_position = (center_x - top_image.w // 2, max(padding, center_y - image_height - padding))
    bottom_position = (center_x - bottom_image.w // 2, min(frame_height - bottom_image.h - padding, center_y + padding))

    # Composite images onto the video
    print_substep("Composite images onto the video")
    video_with_images = CompositeVideoClip([video, top_image.set_position(top_position).set_duration(video.duration), bottom_image.set_position(bottom_position).set_duration(video.duration)])

    # Write the final video to the output file
    print_substep("Writing the final video")
    video_with_images.write_videofile(output_path, codec="libx264", audio_codec="aac", temp_audiofile='temp-audio.m4a', remove_temp=True, fps=fps, preset='ultrafast')


def main(meme_paths, audio_path, video_path, post_title, output):
    print_step("Building video")
    print_start("Setting up")

    # Scrape memes
    print_substep("Checking Meme paths")
    if len(meme_paths) < 2:
        print_error("Insufficient memes collected. Exiting.")
        return
    
    # Setting images
    print_substep("Setting images") 
    top_image_path = meme_paths[0]
    bottom_image_path = meme_paths[1]

    # Scrub title name
    print_substep("Scrubing title name")
    post_title = scrub_text(post_title)

    # Output path for the processed video
    print_substep("Setting output path")
    output_video_path = f"{output}/{post_title}😂.mp4"

    # Convert video to YouTube Shorts format
    convert_video_to_shorts_format(video_path, audio_path, "temp_video.mp4")

    # Add images to the video
    add_images_to_video("temp_video.mp4", top_image_path, bottom_image_path, output_video_path)

    # Clean up temporary video file
    print_substep("Clean up temporary video file")
    os.remove("temp_video.mp4")
