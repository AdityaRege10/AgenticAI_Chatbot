# Agentic AI Chatbot with Knowledge Base and Avatar Lip-Sync

This project is an AI-powered chatbot that processes both text and voice inputs, retrieves information from a knowledge base, and generates both text and speech responses. The chatbot features an interactive avatar using Three.js that lip-syncs with the speech output for a more immersive experience.

## Features

- **Text & Voice Input**: Users can interact using both text and voice.
- **Knowledge Base Integration**: The chatbot retrieves responses from a predefined knowledge base.
- **Speech Output**: Uses text-to-speech (TTS) to generate spoken responses.
- **Avatar Lip-Sync**: A Three.js-based avatar animates according to the chatbot’s speech output.
- **AI Response Generation**: When no predefined response is available, the chatbot generates an answer using AI.

## Technologies Used

### Frontend
- **HTML, CSS, JavaScript** for UI.
- **Three.js** for rendering the lip-syncing avatar.
- **chatbot.js** for handling user interactions.

### Backend
- **Python (FastAPI)** for processing chatbot queries.
- **qachat.py** for querying the knowledge base.
- **Google Text-to-Speech, Whisper API, OpenAI GPT** for AI responses.
- **MongoDB / Firebase** for storing chatbot responses.

## Installation & Setup

### Prerequisites

- **Node.js** (for frontend setup)
- **Python 3.x** (for backend setup)
- **MongoDB / Firebase** (for knowledge base storage)
- API Keys for:
  - Google Text-to-Speech
  - Google Speech-to-Text
  - OpenAI GPT
  - Whisper API

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd geminillmapp
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd geminillmapp
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the `.env` file with API keys and database credentials.
5. Start the backend server:
   ```bash
   uvicorn main:app --reload
   ```

### Database Setup

- Configure and populate MongoDB or Firebase with chatbot responses and knowledge base entries.

## Usage

1. Open the app in your browser.
2. Enter a text query or use voice input.
3. The chatbot will respond with text and voice, and the avatar will lip-sync the speech.

## Contributing

We welcome contributions! Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

