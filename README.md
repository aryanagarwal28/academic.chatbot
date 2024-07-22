# academic.chatbot
This repository displays a chatbot made by using gemini api and other modules to assemble a chatbot capable of answering your questions
How To Use The ChatBot?

This project implements a chatbot using FastAPI and a generative AI model. The chatbot is designed to answer questions specifically related to the Indian education system.

Features:

Generative AI: Utilizes the Gemini Pro model to generate responses.
FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.7+.

Prerequisites:
Python 3.7+
Pipenv (for managing dependencies)

The chatbot is hosted on a local server. Follow these steps to access it:

Ensure the server is running by starting it with the following command in the project directory:

pipenv run uvicorn main:app --host 127.0.0.1 --port 8000
Open your web browser and navigate to:
http://127.0.0.1:8000

Using the Chatbot
Accessing the Chatbot

Open your web browser.
Enter the URL http://127.0.0.1:8000 into the address bar and press Enter.
You will see the chatbot interface.
Interacting with the Chatbot
Ask a Question: Type your question in the text input box at the bottom of the page.
Send the Question: Click the "Send" button or press Enter to submit your question.
Receive a Response: The chatbot will process your question and display a response in the chat window.

FAQ
Q: What kind of questions can I ask the chatbot?
A: You can ask any questions related to the Indian education system, such as information about exams, grading systems, education boards, and more.

Troubleshooting:

No Response from Chatbot
Ensure that the server is running. Refer to the Getting Started section for instructions on starting the server.
Check your internet connection.
Refresh the browser page and try asking your question again.
Unexpected Responses
Make sure your questions are clear and related to the Indian education system.
If the chatbot provides an incorrect response, try rephrasing your question.
