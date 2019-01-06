'''
 tryout Python pyttsx3 package.
 pyttsx3 is an offline Python Text to Speech library.
 
 The following code is tested on a Windows 10 OS + Anaconda
 From Anaconda Prompt first install pyttsx3: pip install pyttsx3
 Then start Jupiter Notebook
 
'''
import pyttsx3;


# Test default speech
engine = pyttsx3.init();
def say(text):
    engine.say(text)
    engine.runAndWait()
say("I see dead people")


# Set Speech rate
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
# Set Speech Volume
engine.setProperty('volume', 0.5)  # Volume 0-1


# Find out what are the voice options on OS 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()


# In my case there where two voices. Create voicelist
en_female_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
en_male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"


# Use male English voice
engine.setProperty('voice', en_male_voice_id)
say("The aliens are coming")


# IMPORT DUTCH VOICE from dutch OS
# https://www.ghacks.net/2018/08/11/unlock-all-windows-10-tts-voices-system-wide-to-get-more-of-them/
NL ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_nlNL_Frank"
BE ="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_nlBE_Bart"


# Test dutch voice
engine.setProperty('voice', NL)
say("als het kalf verdronken is, heeft de koe verdriet.")


# Test Belgium voice
engine.setProperty('voice', BE)
say("Wie het laatst lacht, is traag van begrip.")