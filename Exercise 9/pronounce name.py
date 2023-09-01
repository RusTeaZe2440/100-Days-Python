import pyttsx3

names = ["bhavesh","sahil","dhiru","vedant","tanu"]
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice',voices[1].id) #changes the voice [1] is for female and [0] is for male
def pronounce():
    for i in names:
        engine.say(f"Good Morning {names}")
        engine.runAndWait()
        break
pronounce()
engine.save_to_file(f"Good Morning {names}","names.mp3")
engine.runAndWait()