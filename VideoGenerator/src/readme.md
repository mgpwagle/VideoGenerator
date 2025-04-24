# VideoGenerator

AI Agent to create Videos

## Setup

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (See `requirements.txt` for a list of dependencies.)

2.  **API Keys:**
    *   You will need to obtain API keys for the various AI services used in this project.
    *   Set the API keys as environment variables or directly in the relevant code files (not recommended for security reasons).  Example:
        *   `OPENAI_API_KEY` (used in `story_writing_agent.py`, `video_outline_agent.py`, etc.)
        *   `MUSICGEN_API_KEY` (used in `music_generation_agent.py`)
        *   `IMAGEGEN_API_KEY` (used in `image_generation_agent.py`)
        *   `VOICEGEN_API_KEY` (used in `voice_generation_agent.py`)

## Step 1: Topic Selection

*   The application prompts the user to enter an area of interest for the video (e.g., technology, cooking, travel).
*   The agent then provides several topic suggestions based on the given area.
*   The user selects one topic from the suggestions.

## Step 2: Story Writing

*   A second agent takes the selected topic and generates a story.

## Step 3: Video Outline Generation

*   A third agent refines the story to fit a 5-minute video format, creating a video outline.

## Step 4: Background Music Selection

*   A fourth agent composes background music suitable for the story.

## Step 5: Image Generation

*   A fifth agent generates images based on the story and video outline.

## Step 6: Voice Generation

*   A sixth agent generates voiceovers for the images, based on the story.

## Step 7: Video Generation

*   A seventh agent combines the voiceovers, images, and background music to create the final video.
