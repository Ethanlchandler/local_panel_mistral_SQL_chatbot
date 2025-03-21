import panel as pn  
import ollama
import asyncio

# Start panel
pn.extension()

# Set context for chat
context = """
You are a coding assistant, specifically a data engineer.
"""

# Function to format the chat history for the Mistral model
def apply_template(history):
    history = [message for message in history if message.user != "System"]
    prompt = ""

    for i, message in enumerate(history):
        if i == 0:
            prompt += f"<s>[INST]{context} {message.object}[/INST]"
        else:
            if message.user == "Mistral":
                prompt += f"{message.object}</s>"
            else:
                prompt += f"[INST]{message.object}[/INST]"
    
    return prompt

# Asynchronous function to handle incoming messages and generate responses
async def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
    history = [message for message in instance.objects]
    prompt = apply_template(history)

    # Use asyncio to run the blocking `ollama.chat()` synchronously
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(
        None,  # Use the default thread pool
        lambda: ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )
    )

    # Extract the content from the response
    message = response.get("message", {}).get("content", "")
    
    yield message  # Yield the full message once

# Initialize the chat interface
chat_interface = pn.chat.ChatInterface(
    callback=callback,
    callback_user="Mistral",
)

# Send system message
chat_interface.send("Hello! How can I help you today?", user="System", respond=False)
chat_interface.servable()
