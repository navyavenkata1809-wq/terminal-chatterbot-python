

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot instance
chatbot = ChatBot(
    "TerminalBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"
)

# Create trainer object
trainer = ChatterBotCorpusTrainer(chatbot)

# Train chatbot using English corpus
trainer.train("chatterbot.corpus.english")

print("Training completed successfully.")