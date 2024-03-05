# Personal-Learning-Chat-Bot
This project implements a simple chatbot capable of interacting with users, answering questions based on pre-defined knowledge, learning new information, and performing sentiment analysis on user input.

Files:
chatbot.py: Contains the implementation of the Chatbot class, which handles the main functionalities of the chatbot, including loading and saving data, finding answers to questions, sentiment analysis, handling user input, learning new information, and running the chatbot loop.

knowledge_box: JSON file storing the pre-defined knowledge of the chatbot in the format of questions and answers.

Dependencies:
Python 3.x
Libraries:
json
difflib
textblob
Usage:
Run the chatbot.py script.
The chatbot will greet the user and wait for input.
Enter your query or question.
The chatbot will attempt to provide an answer based on its pre-defined knowledge.
If the chatbot cannot find an answer, it will ask for more information to learn.
To exit the chat, type any of the exit keywords: exit, quit, or bye.

# Description
This project implements a basic chatbot in Python utilizing natural language processing techniques. The chatbot can engage in conversations, answer questions based on pre-existing data, and learn new information from user inputs. It employs sentiment analysis to understand the sentiment behind user inputs and responds accordingly. The chatbot's main features include:

Loading and saving data from a JSON file.
Finding the most suitable answer to a user's query based on similarity.
Analyzing the sentiment of user inputs.
Handling user inputs to provide appropriate responses or learn new information.
Running in a continuous loop until the user decides to exit.
The chatbot provides a simple yet effective demonstration of natural language understanding and conversation handling. It can be extended and customized further to suit specific use cases or integrate with other systems.
