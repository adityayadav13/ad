import pyttsx3
import google.generativeai as genai
import speech_recognition as sr  
genai.configure(api_key="AIzaSyCyVjq9_fhlpoc1_nZgOKD-NVghUnXlhxs")


def gemini():       
     model = genai.GenerativeModel("gemini-1.5-flash")
     prompt = r.recognize_google(audio)
     response = model.generate_content(prompt)

     engine = pyttsx3.init()
     engine.say(response.text)
     engine.runAndWait()
     print(response.text)

while True:
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Kindly voice out your command!")                                                                                   
        audio = r.listen(source)   
        ad=  r.recognize_google(audio)
        if "hello"==ad: 
            engine = pyttsx3.init()
            voices = engine.getProperty('voices') 
            engine.setProperty('voice', voices[1].id) 
            engine.say("initializing " )
            engine.runAndWait()
            print("initializing jd")                                                                      
            while True:
                try:
                     
                     r = sr.Recognizer()                                                                                   
                     with sr.Microphone() as source:                                                                       
                            print("Kindly voice out your command!")                                                                                   
                            audio = r.listen(source)   
                          
                            print( r.recognize_google(audio))
                            gemini()
                           
                except sr.UnknownValueError:
                    print("Apologies, the audio wasn't clear enough.")
        