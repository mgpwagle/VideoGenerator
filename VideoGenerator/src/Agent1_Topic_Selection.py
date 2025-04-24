import os
import openai
from dotenv import load_dotenv

from Agent2_Content_Story_Writing import StoryWriter
from Agent3_Minute_Video_Story_Outline import VideoOutlineGenerator
from Agent4_Background_Music_Selection_Generation import BackgroundMusicSelector
from Agent5_Image_Generation import ImageGenerator
from Agent6_Voice_Generation import VoiceGenerator
from Agent7_Video_Generation import VideoGenerator

class TopicSelector:
    def __init__(self, api_key):
        """
        Initializes the TopicSelector with the OpenAI API key.
        """
        openai.api_key = api_key

    def get_suggestions(self, area):
        """
        Generates a list of YouTube video topics based on the given area.
        """
        prompt = f"Suggest 5 engaging YouTube video topics related to {area} that would attract a wide audience."
        response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # Or "gpt-4"
                messages=[
                    {"role": "system", "content": "You are a helpful YouTube topic generator."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150, #Added max_tokens parameter.
            )
        topics = response.choices[0].text.strip().split('\n')
        return topics

    def display_topics(self, topics):
        """
        Displays the list of suggested topics.
        """
        print("Suggested Topics:")
        for i, topic in enumerate(topics):
            print(f"{i+1}. {topic}")

    def select_topic(self, topics):
        """
        Prompts the user to select a topic from the list.
        """
        selected_topic_index = int(input("Enter the number of the topic you want to select: ")) - 1
        return topics[selected_topic_index]

def main():
    """
    Main function to execute the topic selection and story writing process.
    """
    load_dotenv()
 
    # Fetch the API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # Or "gpt-4"
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."}
                   
                ]
            )
            print(response.choices[0].message.content)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("OpenAI API key not found.")

    if not api_key:
        raise ValueError("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")

    # Step 1: Topic Selection
    topic_selector = TopicSelector(api_key)
    area = input("Enter the area of interest (e.g., technology, cooking, travel): ")
    topics = topic_selector.get_suggestions(area)
    topic_selector.display_topics(topics)
    selected_topic = topic_selector.select_topic(topics)

    # Step 2: Story Writing
    story_writer = StoryWriter(api_key)
    story = story_writer.write_story(selected_topic)

    # Step 3: Video Outline Generation
    video_outline_generator = VideoOutlineGenerator(api_key)
    video_outline = video_outline_generator.create_video_outline(story)
    print("\nVideo Outline:\n", video_outline)

# Step 4: Background Music Selection
    music_selector = BackgroundMusicSelector(api_key)
    music_suggestion = music_selector.find_music(video_outline)
    print("\nMusic Suggestion:\n", music_suggestion)

 # Step 5: Image Generation
    image_generator = ImageGenerator(api_key)
    image_urls = image_generator.generate_images(video_outline)
    print("\nImage URLs:\n", image_urls)
    # Optional: Download images
    images = image_generator.download_images(image_urls)
    print(f"\nDownloaded {len(images)} images.")

    # Step 6: Voice Generation
    voice_generator = VoiceGenerator(api_key)
    voice_script = voice_generator.generate_voice_script(video_outline)
    print("\nVoice Script:\n", voice_script)

  # Step 7: Video Generation
    video_generator = VideoGenerator()
    video_generator.generate_video(images, music_suggestion, voice_script)

    # Display the generated story
    print("\nGenerated Story:\n", story)

if __name__ == "__main__":
    main()


    # Create an instance of the TopicSelector class
topic_selector = TopicSelector()

# Call the select_topic method on the instance
area = input("Enter the area of interest: ")
selected_topic = topic_selector.main() 
print(f"Selected Topic: {selected_topic}")