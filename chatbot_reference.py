# ============================================================
#   GEMINI CHATBOT WITH MEMORY
#   Using: google-genai (new SDK) + dotenv
# ============================================================

# Step 1: Load Dependencies
from google import genai    
from google.genai import types
from dotenv import load_dotenv
import os

# Step 2: Load API Key from .env
load_dotenv()

# Step 3: Create Client (auto-reads GEMINI_API_KEY from env)
client = genai.Client() 

# Step 4: Start a Chat Session (this is what gives it memory)
chat = client.chats.create( 
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="""You are a helpful assistant named Zia.
        You are friendly and give concise answers.
        If the user writes in Urdu, reply in Urdu.
        If the user writes in English, reply in English."""
    )
)

# Step 5: Token counter
total_tokens = 0

# Step 6: Run the Chat Loop
print("=" * 45)
print("        ZIA — Chatbot with Memory")
print("=" * 45)
print("Commands:  'quit' | 'history' | 'tokens'")
print()

while True:

    # Get user input
    user_input = input("You: ").strip()

    # Skip empty input
    if not user_input:
        continue

    # --- COMMANDS ---
    
    if user_input.lower() == "quit":
        print(f"\nSession over. Total tokens used: {total_tokens}")
        print("Khuda Hafiz!")
        break
        
    if user_input.lower() == "history":
        print("\n--- CONVERSATION HISTORY ---")
        for message in chat.get_history():
            role = "You" if message.role == "user" else "Zia"
            # Each message has multiple parts, grab the text
            for part in message.parts:
                print(f"{role}: {part.text}")
        print("----------------------------\n")
        continue

    if user_input.lower() == "tokens":
        print(f"Tokens used this session: {total_tokens}\n")
        continue

    # --- SEND MESSAGE ---
    response = chat.send_message(user_input)

    # Track tokens
    tokens_used = response.usage_metadata.total_token_count
    total_tokens += tokens_used

    # Print reply
    print(f"\nZia: {response.text}")
    print(f"[tokens: {tokens_used} | session total: {total_tokens}]\n")
    
    