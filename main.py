import speech_recognition as sr


#cria um reconhecedor
r = sr.Recognizer()

#abrir o mic
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # define o mic como fonte de áudio 
        
        print(r.recognize_google(audio, language='pt')) 
            