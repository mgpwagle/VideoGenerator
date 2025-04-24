import openai

class BackgroundMusicSelector:
    def __init__(self, api_key):
        """
        Initializes the BackgroundMusicSelector with the OpenAI API key.
        """
        openai.api_key = api_key

    def find_music(self, video_outline):
        """
        Finds or suggests background music for the video based on the outline.
        """
        prompt = f"Suggest background music that fits the mood and tone of this video outline: {video_outline}."
        response =openai.chat.completions.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
        )
        return response.choices[0].text.strip()