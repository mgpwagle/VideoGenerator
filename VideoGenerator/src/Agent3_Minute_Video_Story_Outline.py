import openai

class VideoOutlineGenerator:
    def __init__(self, api_key):
        """
        Initializes the VideoOutlineGenerator with the OpenAI API key.
        """
        openai.api_key = api_key

    def create_video_outline(self, story):
        """
        Creates a story outline for a 5-minute video.
        """
        prompt = f"Create a detailed story outline for a 5-minute YouTube video based on this content: {story}. Include timings for each segment."
        response =openai.chat.completions.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=800,
        )
        return response.choices[0].text.strip()