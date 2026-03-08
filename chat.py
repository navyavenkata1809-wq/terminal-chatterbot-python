
from chatterbot import ChatBot

# Load the trained chatbot
chatbot = ChatBot(
    "TerminalBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"
)

print("Bot is ready. Type 'exit' to stop.")

# Start conversation loop
while True:

    user_input = input("user: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("bot: Goodbye!")
        break

    # Get response from chatbot
    response = chatbot.get_response(user_input)

    print("bot:", response)