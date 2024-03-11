import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("Speak...")
        try:
            audio = recognizer.listen(source, timeout=3)  
        except sr.WaitTimeoutError:
            print("Timeout, no speech detected.")
            continue

    try:
        #Using the Google web speech Api
        recognized_text = recognizer.recognize_google(audio, language='english')
        print("Detected words: " + recognized_text)

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Error with the speech recognition service; {0}".format(e))
