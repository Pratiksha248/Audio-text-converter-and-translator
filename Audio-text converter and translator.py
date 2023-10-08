#Speech-text
import speech_recognition as sr
from deep_translator import GoogleTranslator
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Recognizing...")
        #Recognize speech using the Google Web Speech API
        text = r.recognize_google(audio)
        print("Recognized text (default language):")
        print(text)
        # Translate speech in your desired language
        text_lang = GoogleTranslator(source='auto', target='en').translate(text)
        print(f"Recognized text (translated language):")
        print(text_lang)

#Text-speech
from win32com.client import constants, Dispatch
from deep_translator import GoogleTranslator
Msg = "Ola, como estas!"
speaker = Dispatch("SAPI.SpVoice")
speaker.Speak(Msg)
text_lang = GoogleTranslator(source='auto', target='de').translate(Msg)
speaker.Speak(text_lang)
del speaker
