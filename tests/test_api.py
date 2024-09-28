import unittest
from ghana_nlp.api import GhanaNLP

class TestGhanaNLP(unittest.TestCase):

    def setUp(self):
        # Replace with your valid API key
        self.api_key = "add api key"
        self.nlp = GhanaNLP(api_key=self.api_key)

    def test_translate(self):
        result = self.nlp.translate("Hello", pair="en-tw")
        self.assertNotIn("error", result, "Expected a successful translation, but got an error")

    def test_speech_to_text(self):
        result = self.nlp.stt("your_audio_file.wav", "tw")
        self.assertNotIn("error", result, "Expected successful speech-to-text conversion, but got an error")

    def test_text_to_speech(self):
        result = self.nlp.tts("Hello", lang="tw")
        self.assertNotIn("error", result, "Expected successful text-to-speech conversion, but got an error")

if __name__ == '__main__':
    unittest.main()
