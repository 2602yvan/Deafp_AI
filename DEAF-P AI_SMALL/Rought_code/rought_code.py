import pyttsx3

def speak_it(text):
    engine = pyttsx3.init()  # Fresh engine
    engine.say(text)
    engine.runAndWait()

speak_it("Hello World!")
speak_it("Hello World!")