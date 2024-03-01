from telethon.sync import TelegramClient, events
import datetime
import pandas as pd
import time
import datetime

# Fill in app id and hash, create one on my.telegram.org
api_id = 
api_hash = ""

# put your chat name
chats = [""]

df = pd.DataFrame()

# Function to print messages
def print_new_message(message):
    formatted_message = f"{message.date}\n" \
                        f"{message.text}\n"
    print(formatted_message)

# Initialize the client
client = TelegramClient('botCrawl', api_id, api_hash)

# Event handler for new messages

async def handler(event):
    print_new_message(event.message)

client.add_event_handler(handler, events.NewMessage(chats=chats))

# Start the client
with client:
    client.run_until_disconnected()
