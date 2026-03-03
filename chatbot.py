from google import genai
from dotenv import load_dotenv
from google.genai import types
import os

load_dotenv() # loading api key into file

client=genai.Client() # Makes a client with gemini, so gemini knows this is a client which i will provide service


# This makes a chat which can have multiple messages. Also client makes it remember which person it is chatting to. Here connection made and gemini knows how to behave

chat=client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        system_instruction="""
        You are MindWired. My personal AI chatbot. 
        Your tone should be strict, honest, no false hopes.
        You will reply in short, precise to the point answers
        """,
        temperature=0.7
    )
)

# Making Chatbot
total_token=0

print('-'*45)
print(f'Basic Level Chatbot\nQ to quit.\nT for token')
print('-'*45)

while True:
    user_input=input('You: ').strip() # takes user input using input function

    if not user_input: # So if nothing written, it doesnot do anything.
        continue
    
    # Quit option Chatbot
    
    if user_input.lower()=='q':
        print('Quitting...')
        break
    
    
    # Checking total number of token used in session.
    
    if user_input.lower()=='t':
        print(f'Total Token used:{total_token}')
       
        continue
        
        
        
    # Checking history of chat     
    if user_input.lower()=='h':
        history=chat.get_history()
        for i in history:
            print(f'{i.role}: {i.parts[0].text}')
            

        continue
    
        
        
    
    # Sending user message to gemini and getting back its reply
    response=chat.send_message(user_input)
    print(f'AI: {response.text}')
    
    
    # here response is the variable in which it stores what gemini sends back everything. like text, meta data, usage info and possibly satefy info.add()
    
    
    # usage_meta_data is property that contains info about token usage 
    token_used=response.usage_metadata.total_token_count
    total_token+=token_used
    
    
    # With every chat it prints total token used and used by this chat 
    print(f'Token used in chat {token_used}')
    
    
    

    



