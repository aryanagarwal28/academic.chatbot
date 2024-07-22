import os
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse

# Load environment variables
load_dotenv()

# Configure the Generative AI model with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Pro model and chat
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get a response from the Gemini Pro model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize the FastAPI app
app = FastAPI()

# Serve the main HTML file
@app.get("/")
async def get_index():
    return FileResponse("index.html")

# Handle the message sending
@app.post("/send_message")
async def send_message(request: Request):
    body = await request.json()
    question = body.get("message")
    response = get_gemini_response(question)
    chat_response = ""
    for chunk in response:
        chat_response += chunk.text
    return JSONResponse({"response": chat_response})

# Run the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
