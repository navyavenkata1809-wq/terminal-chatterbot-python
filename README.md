# Terminal Chatbot using Python and ChatterBot

## Overview

This project implements a terminal-based chatbot using Python and the ChatterBot framework. The chatbot is capable of holding simple conversations with users through a command-line interface.

The bot is trained using the ChatterBot English language corpus, which contains various conversational datasets such as greetings, common questions, and general dialogue. The project demonstrates how machine learning-based conversational engines can be integrated into Python applications.

The chatbot learns patterns from conversation datasets and generates responses based on similarity matching and conversational context. This makes it possible to simulate a basic human-like interaction experience.

This project is intended as an educational implementation of a conversational AI system and demonstrates the fundamental concepts behind dialogue systems and natural language processing.

---

# Features

- Terminal-based chatbot interaction
- Machine learning conversation engine
- Training using English conversational corpus
- Automatic response generation
- Persistent conversation database
- Easy to run and modify
- Lightweight command-line application
- Modular Python implementation

---

# Technologies Used

The project is built using the following technologies:

| Technology | Purpose |
|--------|--------|
| Python | Core programming language |
| ChatterBot | Conversational AI engine |
| ChatterBot Corpus | Training dataset |
| SQLite | Local storage for conversations |
| spaCy | Natural language processing support |
| PyYAML | Corpus data parsing |

---

# Project Structure

```
terminal-chatterbot-python/
│
├── chat.py
├── train.py
├── requirements.txt
├── manifest.txt
├── README.md
└── database.sqlite3
```

### File Description

**chat.py**

Main program used to run the chatbot. It allows users to interact with the bot through a terminal interface.

**train.py**

Script used to train the chatbot using the English corpus provided by ChatterBot.

**requirements.txt**

Contains all Python dependencies required to run the project.

**manifest.txt**

Project manifest describing the project information and file structure.

**database.sqlite3**

Automatically generated database that stores conversation statements and responses.

---

# Installation

### Step 1: Clone Repository

```
git clone https://github.com/your-repository-url.git
```

### Step 2: Navigate to Project Folder

```
cd terminal-chatterbot-python
```

### Step 3: Install Dependencies

```
pip install -r requirements.txt
```

### Step 4: Install spaCy Language Model

```
python -m spacy download en_core_web_sm
```

---

# Training the Chatbot

Before running the chatbot, it must be trained using the English conversational dataset.

Run the following command:

```
python train.py
```

During training, the chatbot learns conversation patterns from the corpus files.

Example training output:

```
Training chatterbot.corpus.english.greetings
Training chatterbot.corpus.english.conversations
Training chatterbot.corpus.english.ai
Training completed successfully.
```

---

# Running the Chatbot

After training is complete, the chatbot can be started.

Run:

```
python chat.py
```

The chatbot will start in the terminal.

Example:

```
Bot is ready. Type 'exit' to stop.

user: Hello
bot: Hello

user: How are you?
bot: I am doing very well.

user: exit
bot: Goodbye!
```

---

# Example Interaction

```
user: Good morning
bot: I am doing very well, thank you for asking.

user: What is AI?
bot: Artificial intelligence is the simulation of human intelligence by machines.

user: Do you like hats?
bot: Yes, I like hats.
```

---

# How It Works

The chatbot uses the ChatterBot library which applies machine learning techniques to generate responses.

The system works in three major steps:

1. **Training**
   The bot learns conversational patterns from datasets.

2. **Storage**
   Conversations are stored in a SQLite database.

3. **Response Generation**
   When a user enters text, the bot finds the closest matching statement and generates an appropriate response.

This allows the chatbot to simulate human-like dialogue behavior.

---

# Use Cases

This project demonstrates how conversational AI can be implemented in simple environments.

Possible applications include:

- Learning conversational AI development
- Chatbot prototyping
- Command-line assistants
- Educational AI projects
- NLP experimentation

---

# Requirements

Python 3.9 or higher is recommended.

Required libraries:

```
chatterbot2
chatterbot-corpus
spacy
pyyaml
```

Install them using:

```
pip install -r requirements.txt
```

---

# Future Improvements

Possible enhancements for this project include:

- Adding custom conversation datasets
- Improving response selection algorithms
- Integrating speech recognition
- Creating a web-based chatbot interface
- Deploying the chatbot as an API
- Adding contextual conversation memory

---

# License

This project is intended for educational and demonstration purposes.

---

# Conclusion

This project demonstrates the development of a simple conversational chatbot using Python and ChatterBot. It highlights how machine learning techniques can be applied to natural language conversations and provides a foundation for building more advanced AI-powered dialogue systems.
