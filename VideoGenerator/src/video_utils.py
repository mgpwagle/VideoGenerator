from moviepy import ImageClip, concatenate_videoclips

def generate_video(images, music_suggestion, voice_script, output_file="final_video.mp4"):
    """Generates the final video."""
    clips = []
    for img in images:
        img_clip = ImageClip(np.array(img), duration=5)  # 5-second duration for each image.
        clips.append(img_clip)

    final_clip = concatenate_videoclips(clips, method="compose")

    # This is a placeholder, actual audio processing and insertion will be more complex.
    final_clip.write_videofile(output_file, fps=24)
    print("Video generated successfully!")