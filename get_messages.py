from config import *





# Create the client and connect
async def get_messages():

    await client.start()
    print("Client Created")
    # Ensure you're authorized


    client_dialogs = await client.get_dialogs()
    
    #Insert the contact name, group name , or chat name here
    conversation_title = "Patadevs"
    entity = get_id(client_dialogs,conversation_title)
    
    

    my_entity = await client.get_entity(entity)

    await messages_to_json(my_entity)

   

with client:
    client.loop.run_until_complete(get_messages())