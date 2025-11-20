AI Python Chatbot

A smart command-line interface (CLI) chatbot built with Python. It connects to Large Language Models (LLMs) via the OpenRouter API to provide intelligent responses.
 
Features

• Secure: Uses environment variables to protect API keys.
• Robust: Handles API errors (401, 429) gracefully.
• Clean Output: Parses JSON responses to display only the relevant text.
• Interactive: Continuous chat loop with an easy exit command.

 Technologies

• Python 3.x
• Requests Library
• Python-Dotenv
 Setup and Installation 

 Clone the repository (or download the files)-1

git clone <your-repo-link>
cd your-project-folder
	
2-Install dependencies

pip install -r requirements.txt

3-Configure API Key

Create a new file named .env in the project folder

Add your OpenRouter API key

MY_API_KEY=sk-or-v1-your-key-here

Usage

Run the bot using the terminal

python main.py

Type your message and press Enter

 Type exit or stop or bye to end the chat


Developed by [aziz]