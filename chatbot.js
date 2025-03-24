import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    if (!query.trim()) return; // Avoid empty messages

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", { query });
      setResponse(res.data.response || "No response from AI.");
    } catch (error) {
      console.error("Error:", error);
      setResponse("Error connecting to AI.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-white p-6">
      <div className="w-full max-w-lg bg-gray-800 rounded-3xl shadow-lg p-6 space-y-4">
        <h2 className="text-xl font-semibold text-center text-gray-300">Gemini Chatbot 🤖</h2>
        <div className="flex items-center space-x-2 bg-gray-700 rounded-xl p-3">
          <input
            type="text"
            placeholder="Ask me anything..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="flex-1 bg-transparent text-white placeholder-gray-400 outline-none border-none"
          />
          <button
            onClick={sendMessage}
            className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition"
          >
            Send
          </button>
        </div>
        <div className="bg-gray-700 p-4 rounded-xl min-h-[80px]">
          <strong className="text-gray-400">Gemini:</strong>
          <p className="text-gray-200">{response || "Waiting for a response..."}</p>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;
