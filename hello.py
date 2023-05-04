from gpt4free import Provider, Completion
from gtts import gTTS
import speech_recognition as sr
from pydub import AudioSegment
from pydub.playback import play

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
try:
    recognition = r.recognize_sphinx(audio)
    print("Sphinx thinks you said " + recognition)

    response = Completion.create(Provider.You, prompt=recognition)
    print("###############################")
    print(response)
    
    myObj = gTTS(response)

    filename = recognition.replace(" ", "-")
    myObj.save(filename + "-output.mp3")

    song = AudioSegment.from_mp3(filename + "-output.mp3")
    play(song)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))