# Ghana NLP Python Library 

The **[Ghana NLP API](https://translation.ghananlp.org/) Python Library** provides an easy way to integrate local African language technologies into your Python projects. Whether you're looking for **translation**, **speech-to-text (STT)**, or **text-to-speech (TTS)**, this library makes it simple and intuitive to get started.

## Features

- **Translation**: Translate text between supported African languages (e.g., English to Twi).
- **Speech-to-Text (STT)**: Convert audio files into text.
- **Text-to-Speech (TTS)**: Generate natural-sounding speech from text in local languages.

## Installation

You can install the library directly from PyPI:

```bash
pip install ghana-nlp
```
And update to the lastest version

```bash
python -m pip install --upgrade ghana-nlp
```

## Usage

### Initialize the Library

First, import the library and set your API key:

```python
from ghana_nlp import GhanaNLP

nlp = GhanaNLP(api_key="your_api_key_here")
```

### Translation 

Translate from English to Twi:

```python
result = nlp.translate("Hello, how are you?", language_pair="en-tw")
print(result)  # Wo ho te sɛn?
```

### Speech-to-Text (STT)

Convert an audio file (WAV format) to text:

```python
result = nlp.speech_to_text("your_audio_file.wav", language="tw")
print(result) 
```

### Text-to-Speech (TTS)

Convert text to speech:

```python
result = nlp.text_to_speech("Good morning", lang="tw")
print(result)  # audio binary, write a code to either serve to an audio file or play directly
```

Check this repo to guide you with dealing with audio binary data: [EXAMPLE CODE](https://github.com/PhidLarkson/ghananlp-tts-python)


## Supported Languages

The library supports multiple African languages, including:
- **English (en)**
- **Twi (tw)**
- **Ga (gaa)**
- **Ewe (ee)**
- **Fante (fat)**
- **Dagbani (dag)**, and more!

## Error Handling

The library provides clear error messages if something goes wrong, such as incorrect language codes or invalid API requests. Check the `message` field in the response for details.

## License

This library is licensed under the MIT License.

---

For more details, check out the [documentation](https://pkwolffe.hashnode.dev/ghana-nlp-python-library) and start building cool stuff with **Ghana NLP**! 🎉
