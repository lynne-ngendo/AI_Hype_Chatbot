import openai
import pyttsx3
import time
import os
import streamlit as st

# Retrieve OpenAI API Key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("🚨 ERROR: OpenAI API key is missing! Set it as an environment variable.")
    exit()

openai.api_key = api_key  # Set API Key

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """Make the chatbot speak the response"""
    engine.say(text)
    engine.runAndWait()

def get_gpt_response(prompt):
    """Generate a motivational response using OpenAI's GPT model"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI motivational speaker that gives powerful, confidence-boosting responses."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return "I'm feeling a little off today, but you are still unstoppable! 💪"

def chatbot():
    print("🔥 AI Hype Man Activated! Type 'exit' to stop. 🔥")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("👑 Stay fearless! Chatbot signing off. 👑")
            speak("Stay fearless! Chatbot signing off.")
            break

        # Get AI-generated response
        response = get_gpt_response(user_input)

        print(f"🤖 AI Hype Man: {response}")
        speak(response)

        time.sleep(1)

if __name__ == "__main__":
    chatbot()
