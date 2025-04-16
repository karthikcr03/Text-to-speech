import pyttsx3

def greet_user(name):
   
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

   
    
    engine.setProperty('rate', 150) 
    engine.setProperty('volume', 100.0)  
    
 
    message = f"Hello {name}! Good morning, How are you !"
    
    
    engine.say(message)
    
    engine.runAndWait()


user_name = "Karthik"  
greet_user(user_name)

