# 🎙️ Audio Text Converter and Translator

### Speech-to-Text, Text-to-Speech & Language Translation

An ML-based Python application that converts speech into text, translates it into a desired language, and converts text into speech. The application integrates speech recognition and language translation capabilities to enable seamless communication across different languages.

## ✨ Features

- **Speech-to-Text:** Recognizes spoken words and converts audio input into text.
- **Language Translation:** Translates recognized text into the user's preferred language.
- **Text-to-Speech:** Converts written text into speech output.
- **Speech Translation:** Enables users to translate speech into different languages.
- **Multilingual Support:** Supports multiple languages for translation.

## 🛠️ Tech Stack & Libraries

- **Programming Language:** Python
- **Speech Recognition:** SpeechRecognition
- **Language Translation:** DeepTranslator
- **Text-to-Speech:** pywin32 (Windows SAPI)
- **Environment:** Jupyter Notebook

## ⚙️ How It Works

1. The user provides audio input through a microphone.
2. SpeechRecognition captures and recognizes the spoken words.
3. The recognized speech is converted into text.
4. DeepTranslator translates the text into the selected target language.
5. Users can also enter text to translate it into another language.
6. The translated text is converted into speech output.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Pratiksha248/Audio-text-converter-and-translator.git

cd Audio-text-converter-and-translator
```

### 2. Install Dependencies

Install all required libraries:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

**Option 1: Using Python**

```bash
python "Audio-text converter and translator.py"
```

**Option 2: Using Jupyter Notebook**

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open `Audio-text converter and translator.ipynb` and execute the cells sequentially.

## 🎯 Project Objective

To develop a Python-based speech and text conversion system that simplifies multilingual communication by integrating speech recognition, language translation, and text-to-speech technologies.
