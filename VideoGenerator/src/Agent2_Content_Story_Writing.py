import openai

class StoryWriter:
    def __init__(self, api_key):
        """
        Initializes the StoryWriter with the OpenAI API key.
        """
        openai.api_key = api_key

    def write_story(self, topic):
        """
        Writes a story or content based on the selected topic.
        """
        prompt = f"Write a compelling story or script for a YouTube video about: {topic}."
        response = openai.chat.completions.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
        )
        return response.choices[0].text.strip()