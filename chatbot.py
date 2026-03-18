"""
Use your API key from Google AI Studio. Store it in .env file
install libraries using 
pip install google-genai python-dotenv.
Never share your API key with anyone.
Always use env file to store it and necer upload env file to github.
Happy Coding!
"""


from google import genai
from dotenv import load_dotenv
import os
from google.genai import types
import json


load_dotenv()

# Connection with LLM (Gemini)
client=genai.Client()


def load_history():
        data=[]
        if os.path.exists('history.json'):
            with open('history.json','r') as f:
              data=json.load(f)
            history=[]
            for i in data:
                history.append(
                    types.Content(
                        role=i['role'],parts=[types.Part(text=i['content'])]))  
            return history
        return []

def save_history():
    history=chat.get_history()
    data=[]
    for i in history:
        data.append(
            {'role':i.role,'content':i.parts[0].text}
        )
    with open('history.json','w') as f:
        json.dump(data,f)

chat=client.chats.create(
    
    model='gemini-2.5-flash',
    history=load_history(),
    config=types.GenerateContentConfig(
        system_instruction="Your name is Mindwired. You will reply me in short sentences okay"))
 

# Making chatbot

print('-'*45)
print('Welcome to Chatbot\nPress Q to quit\nH for history\nT for token')
print('-'*45)

total_token=0
    
while True:
    user_input=input('You: ').strip()
    
    
    if not user_input:
        continue
    
    # Check History 
    
    if user_input.lower()=='h':
     
        history=chat.get_history()
    
        for i in history:
            print(f'{i.role}: {i.parts[0].text}')

    # Checking quit button
    
    elif user_input.lower()=='q':
        break
    
    # Check no of token used
    
    elif user_input.lower()=='t':
        response=chat.send_message(user_input)
        token_used=response.usage_metadata.total_token_count
        total_token+=token_used
        
        print(f'Token used: {token_used}')
    else:
        response=chat.send_message(user_input)
        save_history()
        print(f'AI: {response.text}')  
        
     
    print('-'*45) 
    
   
    
    
    