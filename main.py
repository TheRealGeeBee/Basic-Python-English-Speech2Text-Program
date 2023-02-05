"""Credits: Gabriel Onyedika Nnamoko
Sophomore student of Electronics and Computer Engineering, Nnamdi Azikiwe University Awka, Nigeria.
Done in partial fulfillment for the course requirements for ECE331 (Signals and Systems).
Lecturers: Dr. Ogwugwam Ezeagwu and Engr. Peace Obioma
February, 2023"""


import speech_recognition as sr #Importing the required algorithm for speech recognition

recognizer = sr.Recognizer()

''' The algorithm listens to the audio file '''

with sr.AudioFile("Test File.wav") as source:
    recorded_audio = recognizer.listen(source)
    print("I have listened to the end!")

    ''' Recognizing the Audio '''
try:
    print("\nDeciphering this audio...")
    text = recognizer.recognize_google(
            recorded_audio,
            language="en-US"
        ) #Uses the recognize_google module (from Google) to recognize spoken speech
    print("Here's what the guy in the audio said : {}".format(text)) #Prints out text version of audio

except Exception as ex:
    print(ex)