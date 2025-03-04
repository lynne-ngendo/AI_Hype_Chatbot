import random
import time
import pyttsx3  # Import Text-to-Speech library

# Initialize the TTS engine
engine = pyttsx3.init()

# Dictionary of motivational responses
motivational_quotes = {
    "motivate me": [
        "You are powerful beyond measure!",
        "Nothing can stop you. You were made to win!",
        "Success is already yours. Just claim it!",
        "Keep moving forward – the world is waiting for you!",
        "You were not given a spirit of fear, but of power!"
    ],
    "i feel stuck": [
        "Break the chains – you are limitless!",
        "Being stuck is an illusion. Take action and create momentum!",
        "Fear is a lie. You’ve conquered harder things before!",
        "Every challenge is a setup for your next level. Keep pushing!"
    ],
    "i can't do this": [
        "Yes, you can! And you will!",
        "You are already equipped with everything you need to win!",
        "Remember why you started – quitting is not an option!",
        "Step by step, you’re already making progress!"
    ]
}


def speak(text):
    """Function to make the chatbot speak"""
    engine.say(text)
    engine.runAndWait()


def chatbot():
    print("🔥 AI Hype Man Activated! Type 'exit' to stop. 🔥")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("👑 Stay fearless! Chatbot signing off. 👑")
            speak("Stay fearless! Chatbot signing off.")
            break

        response = None
        for key in motivational_quotes:
            if key in user_input:
                response = random.choice(motivational_quotes[key])
                break

        if response:
            print(f"🤖 AI Hype Man: {response}")
            speak(response)  # Make the chatbot speak the response
        else:
            print("🤖 AI Hype Man: I see you grinding! Keep going! 💪")
            speak("I see you grinding! Keep going!")

        time.sleep(1)  # Adds a slight delay for a natural conversation feel


if __name__ == "__main__":
    chatbot()
