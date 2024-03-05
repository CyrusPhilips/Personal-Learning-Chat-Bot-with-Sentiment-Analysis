Chatbot Project
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