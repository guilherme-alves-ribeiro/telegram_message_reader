import configparser
import json
from telethon import TelegramClient
from telethon.tl.functions.messages import (GetHistoryRequest)


# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash)

def get_dialog(dialogs,name):
        for dialog in dialogs:
            if dialog.title == name:
                return dialog.dialog
        return False
    

def get_id(dialogs,name):

        conversation = get_dialog(dialogs,name)
        if(conversation != False):
            return conversation.peer
        return None

async def messages_to_json(entity):
    offset_id = 0
    limit = 100
    all_messages = []
    total_messages = 0
    total_count_limit = 0

    while True:
        print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
        history = await client(GetHistoryRequest(
            peer=entity,
            offset_id=offset_id,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:
            all_messages.append(message.to_dict())
        offset_id = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if total_count_limit != 0 and total_messages >= total_count_limit:
            break
    message_dict= {}
    for message in all_messages:
        if message["_"] == "Message":
            message_dict[message["id"]] = message["message"]

    with open('messages.json', 'w') as outfile:
        
            json.dump(message_dict, outfile, ensure_ascii=False)