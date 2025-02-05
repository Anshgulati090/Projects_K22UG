#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#quiz application built using Python and the tkinter library. 
#It allows users to test their knowledge of Python programming with a series of multiple-choice questions. 
#Users can answer questions, track their scores, and view correct answers for questions they've answered incorrectly.

#Features
Interactive quiz interface.
Timer to complete the quiz.
Score tracking and display.
Review of incorrect answers.
Restart or retake the quiz.
Prerequisites
Python 3.x installed on your computer.

#Timer Functionality

The Python Quiz App includes a timer feature that adds an element of challenge to the quiz-taking experience. 
Here's how it works:

#Countdown Timer: 
When a user starts a quiz, a countdown timer is initiated with a default time limit of 30 seconds for each question.

#Visual Indication: 
The timer is displayed on the user interface, allowing the user to keep track of the remaining time.

#Timer Color Changes:
The timer color changes to red when there are less than 10 seconds remaining, providing a visual alert.

#Button Color Changes:
The color of the "Next" and "Finish Test" buttons also changes based on the remaining time, 
with "Next" button turning green and "Finish Test" button turning red when needed.

#Auto Submission: 
If the timer reaches zero while a question is unanswered, the quiz is automatically submitted,
ensuring that users complete the quiz within the time limit.

#User Experience:
The timer adds an element of excitement to the quiz and encourages users to answer questions promptly.


# In[ ]:


import tkinter as tk
from tkinter import messagebox
import json

# Define a class QuizApp
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")
        
        # Load questions from a JSON file
        self.questions = self.load_questions("questions.json")
        
        # Initialize variables
        self.current_question = 0
        self.score = 0
        self.selected_option = tk.StringVar(value=None)
        self.wrong_answers = []
        self.score_window = None
        self.timer = 30
        self.timer_id = None

        # Set the initial window geometry to full screen
        root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        # Create and pack the question label
        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack()

        # Create and pack the option buttons
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(root, text="", variable=self.selected_option, value=str(i+1))
            self.option_buttons.append(option_button)
            option_button.pack()

        # Create and pack the "Next" button
        self.next_button = tk.Button(root, text="Next", command=self.check_answer, fg="black")  # Initialize as black
        self.next_button.pack()

        # Create and pack the "Finish Test" button
        self.finish_button = tk.Button(root, text="Finish Test", command=self.finish_test, fg="black")  # Initialize as black
        self.finish_button.pack()

        # Create and pack the score label
        self.score_label = tk.Label(root, text="")
        self.score_label.pack()

        # Create and pack the timer label
        self.timer_label = tk.Label(root, text="", font=("Arial", 14), fg="black")  # Initialize as black
        self.timer_label.pack(side=tk.RIGHT)

        # Load the first question and start the timer
        self.load_next_question()
        self.update_timer()

    # Function to load questions from a JSON file
    def load_questions(self, filename):
        with open(filename, 'r') as file:
            questions = json.load(file)
        return questions

    # Function to load the next question
    def load_next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            question_text = question_data["question"]
            options = question_data["options"]
            self.correct_answer = question_data["correct_answer"]
            self.question_label.config(text=f"Q{self.current_question + 1}: {question_text}")
            for i, option_button in enumerate(self.option_buttons):
                option_button.config(text=options[i])
            self.selected_option.set(None)
        else:
            self.submit_quiz()

    # Function to check the selected answer
    def check_answer(self):
        if self.selected_option.get():
            selected_answer = int(self.selected_option.get())
            if selected_answer == self.correct_answer:
                self.score += 1
            else:
                self.wrong_answers.append(self.current_question + 1)
            self.current_question += 1
            self.load_next_question()

    # Function to submit the quiz
    def submit_quiz(self):
        self.show_score_and_wrong_answers()
        self.next_button.config(state="disabled")
        self.finish_button.config(state="disabled")
        self.timer_label.config(text="Time's up!")
        self.stop_timer()

    # Function to display the score and wrong answers
    def show_score_and_wrong_answers(self):
        score_text = f"Your score: {self.score}/{len(self.questions)}"
        wrong_answers_text = ""
        if self.wrong_answers:
            wrong_answers_text = "\nWrong Answers:\n"
            for question_number in self.wrong_answers:
                question_data = self.questions[question_number - 1]
                question_text = question_data["question"]
                correct_answer = question_data["options"][question_data["correct_answer"] - 1]
                wrong_answers_text += f"Q{question_number}: {question_text}\nCorrect Answer: {correct_answer}\n"

        # Create a new window to display the score
        self.score_window = tk.Toplevel(self.root)
        self.score_window.title("Quiz Score")
        score_label = tk.Label(self.score_window, text=score_text + wrong_answers_text, font=("Arial", 14))
        score_label.pack()

        # Create a button to retake the quiz
        retry_button = tk.Button(self.score_window, text="Retake Quiz", command=self.restart_quiz)
        retry_button.pack()

    # Function to restart the quiz
    def restart_quiz(self):
        self.current_question = 0
        self.score = 0
        self.wrong_answers = []
        self.next_button.config(state="active")
        self.finish_button.config(state="active")
        self.score_label.config(text="")
        self.timer = 30
        self.load_next_question()
        self.update_timer()

        # Hide the score window (if it exists) without closing it
        if self.score_window and self.score_window.winfo_exists():
            self.score_window.withdraw()

    # Function to finish the quiz
    def finish_test(self):
        self.submit_quiz()

    # Function to update the timer
    def update_timer(self):
        if self.timer > 0:
            # Change timer color to red when it's less than 10 seconds
            timer_color = "red" if self.timer < 10 else "black"
            self.timer_label.config(text=f"Time Left: {self.timer} sec", fg=timer_color)
            
            # Change next button and finish button colors
            next_button_color = "green" if self.timer > 10 else "black"
            finish_button_color = "red" if self.timer <= 10 else "black"
            
            self.next_button.config(fg=next_button_color)
            self.finish_button.config(fg=finish_button_color)
            
            self.timer -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        elif self.timer == 0:
            self.submit_quiz()
            self.timer = -1

    # Function to stop the timer
    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

if __name__ == "__main__":
    # Create a Tkinter window and initialize the QuizApp
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


# In[ ]:


#The code defines a QuizApp class using the Tkinter library in Python for creating a quiz application.

#The application loads questions from a JSON file named "questions.json" to populate the quiz.

#It initializes variables such as the current question number, score, a variable to track the selected option,
a list to store wrong answers, and a timer set to 30 seconds.

#The GUI layout is created with labels for questions, radio buttons for answer options, 
and buttons for navigating to the next question or finishing the quiz.

#The "Next" button advances to the next question, checking and updating the score based on the selected answer.

#A "Finish Test" button allows the user to submit the quiz before completing all questions.

#A timer is implemented to limit the time for answering each question. 
The timer updates dynamically, and the color changes to red when it's less than 10 seconds.

#The application tracks wrong answers and displays the final score along with details of any
incorrect answers after completing the quiz.

#A separate window is created to display the quiz score along with an option to retake the quiz.

#The code includes functions to restart the quiz, finish the quiz, update the timer, and stop the timer when needed.

#The main block initializes the Tkinter window and creates an instance of the QuizApp class, 
starting the application loop with root.mainloop().


# In[ ]:


#explanation of the code:

#Class Definition (QuizApp): The code begins by defining a class named QuizApp that represents the quiz application.

#Initialization Method (__init__): The __init__ method initializes the attributes and sets up the main window using Tkinter. 
    It loads quiz questions from a JSON file, initializes variables for tracking the current question, score, selected option, wrong answers, and sets up the timer.

#GUI Layout:

The GUI layout is created with labels for questions, radio buttons for answer options, and
buttons for navigating to the next question or finishing the quiz.
The "Next" button advances to the next question, and a "Finish Test" 
button allows the user to submit the quiz.

#Question Loading (load_questions and load_next_question): 
    The load_questions method reads questions from a JSON file.
    The load_next_question method updates the GUI with the next question's details.

#Answer Checking (check_answer): The check_answer method is called when the user selects an answer. 
It updates the score based on the correctness of the chosen answer and advances to the next question.

#Quiz Submission (submit_quiz): The submit_quiz method is called when the quiz is finished. 
It displays the final score and wrong answers, disables further interaction, and stops the timer.

#Score Display (show_score_and_wrong_answers): This method creates a new window to display
the user's score and any wrong answers. It also provides a button to retake the quiz.

#Quiz Restart (restart_quiz): The restart_quiz method resets the quiz variables, 
enabling the user to retake the quiz.

#Timer Functionality (update_timer and stop_timer):

The update_timer method dynamically updates the timer display and changes color based on time remaining.
It also adjusts the colors of the "Next" and "Finish Test" buttons.

The stop_timer method cancels the timer when needed.

#Main Block (__main__): The script creates a Tkinter window and initializes an instance of 
    the QuizApp class, starting the application loop with root.mainloop().

