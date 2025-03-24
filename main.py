import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv("api.env")
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API key exists
if not API_KEY:
    print("Error: API key not found. Set the GEMINI_API_KEY environment variable.")
    exit()

# Configure GenAI with the correct API key
genai.configure(api_key=API_KEY)

# Check if API key is working
try:
    models = genai.list_models()
    print("✅ API Key is working! Available models:")
    for m in models:
        if 'generateContent' in m.supported_generation_methods:
            print("-", m.name)
except Exception as e:
    print("❌ Error while verifying API key:", e)
    exit(1)  # Exit if API key validation fails

# Initialize the model
model = genai.GenerativeModel("gemini-2.0-flash")

# Start a chat session
chat = model.start_chat(history=[])

print("\nGemini Chatbot 🤖 - Type 'exit' to stop.\n")

while True:
    prompt = input("You: ").strip()
    if prompt.lower() == "exit":
        print("Goodbye! 👋")
        break

    try:
        response = chat.send_message(prompt)
        print("Gemini:", response.text)
    except Exception as e:
        print("❌ Error:", e)
