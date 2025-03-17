import speech_recognition as sr   # type: ignore

def voice_input():  
    recognizer = sr.Recognizer()  
    with sr.Microphone() as source:  
        print("Listening...")  
        audio = recognizer.listen(source)  
        try:  
            text = recognizer.recognize_google(audio)  
            return text  
        except sr.UnknownValueError:  
            return "Sorry, could not understand."