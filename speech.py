import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('speak anything')
    r.pause_threshold = 1
    audio=r.listen(source)
    try:
        
        text=r.recognize_google(audio)
        print('you said:',format(text))
    except:
        print('sorry could not recognize')
