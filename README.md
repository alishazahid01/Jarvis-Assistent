The "Jarvis Assistant" is a simple voice-activated assistant program implemented in Python. It uses the pyttsx3 library for text-to-speech conversion, speech_recognition (SpeechRecognition) for speech recognition, and can perform various actions based on voice commands. Below is a detailed explanation of how the code works:
Code Structure and Functionality:
    1. Initialization and Setup:
        ◦ The code begins by importing the necessary libraries and initializing the text-to-speech engine using pyttsx3.
    2. speak Function:
        ◦ The speak function takes a text message as input and both prints and vocalizes the message using the text-to-speech engine.
    3. listen Function:
        ◦ The listen function initializes a speech recognizer (Recognizer) and captures audio input from the microphone.
        ◦ It sets the energy threshold and dynamic energy threshold for audio recognition.
        ◦ The recognized speech is converted to text using Google's speech recognition API.
        ◦ Exceptions are handled for unrecognized and request errors, and an empty string is returned in such cases.
    4. perform_action Function:
        ◦ The perform_action function takes the recognized user query as input and performs specific actions based on the query.
        ◦ It runs in a loop, continually listening for user queries until the user says "goodbye."
    5. Main Section (if __name__ == "__main__":):
        ◦ The main section initiates the conversation with a greeting from Jarvis.
        ◦ It enters a loop where it listens for user queries using the listen function and responds accordingly using the perform_action function.
        ◦ The conversation continues until the user says "goodbye."
Supported Commands and Actions:
    • Greeting: Jarvis responds to "hello" with a greeting.
    • Inquiry About Well-being: Jarvis responds to "how are you" with a reply.
    • Time: Jarvis provides the current time when asked.
    • Search: Jarvis performs a Google search when the user provides a search query after saying "search."
    • Goodbye/Exit: Jarvis says goodbye and exits the program when the user says "goodbye" or "exit."
How the Code Works:
    1. The script initializes the speech recognition and text-to-speech engines.
    2. It starts a continuous conversation loop:
        ◦ Listens for user input using the microphone.
        ◦ Converts the user's speech to text.
        ◦ Performs actions based on recognized commands.
        ◦ Continues the loop until the user says "goodbye."
    3. Recognized queries trigger specific actions such as greetings, providing the current time, performing web searches, or saying goodbye.
    4. The script provides vocal responses to the user's queries and actions.
Note:
    • The pyttsx3 library is used for text-to-speech synthesis.
    • The speech_recognition library handles speech recognition using Google's speech recognition API.
    • While this script provides basic voice interaction and limited functionality, it can be extended to include more advanced features and commands.
Please note that for voice recognition to work, you need an active internet connection, as it relies on Google's speech recognition service. Additionally, you may need to install the required libraries (pyttsx3 and SpeechRecognition) using pip if not already installed.
