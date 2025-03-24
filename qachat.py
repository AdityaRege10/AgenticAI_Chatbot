import os
import tempfile
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from gtts import gTTS

response = ""

# Load environment variables
load_dotenv()

# Configure the Gemini model
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("API key not found. Set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to get predefined response from the text file
def get_predefined_response(user_input):
    try:
        with open("responses.txt", "r", encoding="utf-8") as file:  # Specify UTF-8 encoding
            content = file.read()
        faqs = content.split("Q")
        for faq in faqs:
            if user_input.lower() in faq.lower():
                if "A:" in faq:
                    return faq.split("A:")[1].strip()
        return None
    except FileNotFoundError:
        return None
    except UnicodeDecodeError as e:
        return f"Error reading the file: {e}"


# Function to get Gemini response
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit UI Configuration
st.set_page_config(page_title="qubit_ai")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #ff6f61, #5f77ff);
        color: white;
    }
    .stApp {
        background: linear-gradient(120deg, #ff6f61, #5f77ff);
        color: white;
    }
    .header {
        text-align: center;
        font-size: 4rem;
        font-weight: bold;
        background: linear-gradient(90deg, #b0c4de, #d3d3d3, #b0c4de);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
    }
    .response-box {
        font-size: 1.5rem;
        padding: 20px;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.1);
        max-height: 300px;
        overflow-y: auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="header">SOPHOS</div>', unsafe_allow_html=True)
st.markdown(
    f"""
    <style>
        .iframe-container {{
            margin: 0 auto;
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 0;
        }}
        iframe {{
            border: none;
            border-radius: 15px;
            width: 800px;
            height: 600px;
        }}
        .iframe-spacing {{
            margin-bottom: 30px; /* Add space below the iframe */
        }}
    </style>
    <div class="iframe-container iframe-spacing">
        <iframe
            src="http://localhost:5175/?text={response}"
        ></iframe>
    </div>
    """,
    unsafe_allow_html=True,
)


# Input area
col1, col2 = st.columns([4, 1])
with col1:
    user_input = st.text_input("", placeholder="Input your question...", key="input", label_visibility="collapsed")
 
with col2:
    button_clicked = st.button("Ask", key="ask_button")
  

# Language selection dropdown
languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
}
selected_language = st.selectbox("Select Narration Language", options=list(languages.keys()), index=0)

if button_clicked and user_input:
    # Get response
    response = get_predefined_response(user_input)
    if not response:
        response = get_gemini_response(user_input)
    
    # Display response
    st.markdown('<div class="response-box"><strong>The response is:</strong></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)
    
    # Generate narration in the selected language
    if response:
        lang_code = languages[selected_language]
        try:
            tts = gTTS(text=response, lang=lang_code)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                tts.save(temp_audio.name)
                st.audio(temp_audio.name, format="audio/mp3")
        except Exception as e:
            st.error(f"Error generating audio in {selected_language}: {e}")
