import openai
import pyttsx3
import os
import streamlit as st

# Retrieve OpenAI API Key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("🚨 ERROR: OpenAI API key is missing! Set it as an environment variable.")
    st.stop()

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

# Streamlit Web Interface
st.title("🔥 AI Hype Man – Your Personal Motivational Chatbot 🔥")

st.write("Type your thoughts below and let the AI Hype Man inspire you! 😏")

user_input = st.text_input("You:", "")

if st.button("Get Motivation"):
    if user_input:
        response = get_gpt_response(user_input)
        st.write(f"🤖 AI Hype Man: {response}")
        speak(response)
    else:
        st.warning("Please enter a message first!")
