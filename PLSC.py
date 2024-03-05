# Importing required libraries
import json
from difflib import SequenceMatcher
from textblob import TextBlob
import random

# Defining the Chatbot class
class Chatbot:
    def __init__(self, data_file):
        # Constructor to initialize the Chatbot
        self.data_file = data_file
        self.knowledge_box = self.load_data()  # Loading data from the specified file

    # Method to load data from a JSON file
    def load_data(self):
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"File '{self.data_file}' not found.")
            return None

    # Method to save data to the JSON file
    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.knowledge_box, f, indent=4)

    # Method to find the best matching answer for a given question
    def get_answer(self, question):
        max_similarity = 0
        matched_question = None
        
        for category in self.knowledge_box['categories']:
            for item in category['questions']:
                similarity = SequenceMatcher(None, question.lower(), item['question'].lower()).ratio()
                if similarity > max_similarity:
                    matched_question = item
                    max_similarity = similarity
        
        if matched_question and max_similarity >= 0.5:
            return matched_question['answer']
        else:
            return None

    # Method to analyze sentiment of a given text
    def analyze_sentiment(self, text):
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        if sentiment_score > 0:
            return "positive"
        elif sentiment_score < 0:
            return "negative"
        else:
            return "neutral"

    # Method to handle user input
    def handle_user_input(self, user_input):
        if user_input.lower() in self.exit_keywords:
            print("Bot: Goodbye!")
            return False
        
        answer = self.get_answer(user_input)
        sentiment = self.analyze_sentiment(user_input)

        if answer:
            print("Bot:", answer, f"({sentiment} sentiment)")
        else:
            print("Bot: I'm not sure about that. Let me check...")
            # Simulate thinking time
            print("Bot: ...")
            print("Bot:", random.choice(["I'm sorry, I couldn't find an answer.",
                                         "I'll need to learn more about that.",
                                         "Can you provide more information?"]))
            # Learn new information
            self.learn_new_info(user_input)

        return True

    # Method to learn new information
    def learn_new_info(self, question):
        new_answer = input("Bot: What's the answer to that question? ").strip()
        new_question_entry = {"question": question, "answer": new_answer}
        self.knowledge_box['categories'][0]['questions'].append(new_question_entry)
        self.save_data()
        print("Bot: Thanks for teaching me!")

    # Method to run the chatbot
    def run(self):
        if self.knowledge_box is None:
            return
        
        self.exit_keywords = ['exit', 'quit', 'bye']
        
        print("Bot: Hi! I'm your friendly chatbot. How can I help you today?")
        
        while True:
            user_input = input("You: ").strip()
            if not self.handle_user_input(user_input):
                break

# Entry point of the program
if __name__ == "__main__":
    # Creating an instance of the Chatbot class
    # Specify the path to the data file knowledge box
    chatbot = Chatbot(data_file='knowledge_box path')
    # Run the chatbot
    chatbot.run()