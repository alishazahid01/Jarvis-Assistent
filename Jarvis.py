# Jarvis assistant
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

engine = pyttsx3.init()

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 12610 
    recognizer.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        print("Listening......")
        audio = recognizer.listen(source)
        try:
            user_query = recognizer.recognize_google(audio)
            print(f"User: {user_query}")
            return user_query.lower()  # Convert to lowercase to make comparisons easier
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError as e:
            print(f"Sorry, there was an error with the speech recognition. Error: {e}")
            return ""

def perform_action(query):
    while True:  # Run the loop until the user says "goodbye"
        if "hello" in query:
            speak("Hello! How can I assist you?")

        elif "how are you" in query:
            speak("I'm just a computer program, but I'm here and ready to assist you!")
        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        elif "search" in query:
            search_term = query.replace("search", "").strip()
            if search_term:
                url = f"https://www.google.com/search?q={search_term}"
                webbrowser.open(url)
                speak(f"Here are the search results for {search_term}.")
            else:
                speak("Please specify something to search for.")
        elif "goodbye" in query or "exit" in query:
            speak("Thankyou for using Jarvis. Goodbye!")
            exit()
        else:
            speak("I'm not sure how to help with that.")
        query = listen()  # Listen to the user's reply

if __name__ == "__main__":
    text = "Hi! I'm Jarvis. How can I assist you?"
    speak(text)

    while True:  # Main loop to keep the conversation going until "goodbye"
        user_query = listen()
        perform_action(user_query)
