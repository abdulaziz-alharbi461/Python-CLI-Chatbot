import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
my_key = os.getenv("MY_API_KEY") 


print("\nthe chatbot is on!\n")
print("write exit or stop or bye to end the chat \n")

while True:
    user_input = input("YOU: ")

    if user_input.strip() == "stop" or user_input.strip() == "exit" or user_input.strip() == "bye":
        print("Good bye Have nice day!")
        break

    if not user_input.strip():
        continue

    headers = {
        "Authorization": f"Bearer {my_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost", 
        "X-Title": "My chatbot",
    }
    
    data = {
        "model":"google/gemma-3-4b-it:free",#the model
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        print("Thinking...")
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            data=json.dumps(data)
        )

        if response.status_code == 200:
            
            raw_answer = response.json()['choices'][0]['message']['content']
            clean_answer = raw_answer.replace("[/s]", "").replace("<s>", "").strip()
            
            print(f"Chatbot: {clean_answer}\n")
            print("-" * 30) 
           
            if not raw_answer or raw_answer.isspace():
                print("Chatbot: please try again")
            
        elif response.status_code == 401:
            print("error 401")
            break 
            
        else:
            print(f" error {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"lost the connection!{e}")