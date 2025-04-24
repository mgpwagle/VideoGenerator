import openai

class VoiceGenerator:
    def __init__(self, api_key):
        """
        Initializes the VoiceGenerator with the OpenAI API key.
        """
        openai.api_key = api_key

    def generate_voice_script(self, video_outline):
        """
        Generates a voiceover script for the video content based on the outline.
        """
        prompt = f"Generate a voiceover script for the video outline: {video_outline}."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
        )
        return response.choices[0].text.strip()