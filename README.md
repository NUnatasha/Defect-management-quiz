# Defect-management-quiz
this is my summative two code for IFCP course, year one

## Order of Documentation
1. Introduction
2. Design
3. Development
4. Testing
5. User Documentation
6. Evaluation 

# Introduction
As new websites, apps and software system become increasingly more important to businesses so does the need to ensure their quality. Especially, when these applications are heavily relied on and made to provide efficiency or be a key part of the business' functionality. It is critical that these applications are efficient, reliable and are provide a postive and great customer experience. 

In my role as defect manager and working within the IBM test team I have noticed the lack of knowledge around defects. How should they be handled? How do they get resolved? Who is working on this and so on. Questions like this frequently come up and it is down to the lack of knowledge around defect management. This is why providing short training on defect management would lead to faster resolution time, clear and neccessary commiunication and better organisation. It would also benefit new members who are unaware of how we operate and work with these defects

The Software Development Life Cycle (SDLC) includes the important part of testing; and defect managemnmet plays a key role in that. As you perform functional testing, regression testing, unit testing, system testing and User Acceptance Testing (UAT), etc bugs and defects are going to found. Defect managemnet can ensure that these bugs/defects are identified correctly, tracked and auditted properly, prioritised during testing. Making sure that the relevant employees have a strong understanding and knowledge around this proccess can help reduce mistakess, improve quality of software and have effective collaboration for the resolution

This project is a simple multiple choice quiz using python(https://www.python.org) and Tkinter (https://docs.python.org/3/library/tk.html). The purpose of this quiz application is to test the user on their knowledge on defect Management and to provide training. Five qustions multiple choice questions are displayed one at a time allow the user to select one option out of four.

# Design 
## Figma Design
This is the initial design for the quiz. The user would be greeted with a welecome screen in which they are instructed to enter their name. Then one question will show up at a time, displaying the question at the top and the four option buttons beneath. Once the user clicked an option the feedback will be shown either "Correct" or "Incorrect" and move onto the next question. Each time the score would be calculated and show in the left-bottom corner. Initially I had designe the user journey to only be a few simple steps:
1. Open app
2. Enter name and submit
3. Click your choice
4. Repeat step 3 until end of quiz

![Defect Managemnet Figma Design](image.png)

I have slighly changed from the initial design. Instead the user is allowed to change go to the next question on their own accord. I decided this so that the user can then review the question and try understand as to why the may have gotten it wrong instead of immediately switch to the next question and not having any time memorise or learn. 


## Functional Requirements
1. Load questions from a CSV file
2. Display GUI
3. Allow the user to select their choice
4. Feedback is shown 
5. The score is tracked and shown at the bottom of the page
6. When Next button is clicked the next question is displayed
7. save the results to a csv file

## Non-Functional Requirements
1. Easy to use UI
2. Fast response time 
3. Maintainable code
4. Readable code

## Tech Stack

List of programming languages amnd libaries used to create the quiz.

| Technology | Purpose |
|------------|---------|
|Python| Programming Language used to code app|
|Tkinter| GUI, used to create Graphical User. Interface|
|CSV|Used to load data from and and input data into|
|unitest|Used to perform automated test|

## Class Diagram
![class diagram](image-1.png)

# Developnment

## Project Structure
 Defect-Management--uiz-summative-two
 |
 |--main.py
 |--question.csv
 |--quiz_data.py
 |--results.csv
 |--test_smoke_and_all.py

## Loading questions
 The questions are stored in a CSV file which is pulled and loaded into python using a function called load_questions.
 CSV structure: questions,option1,option2,option3,option4,answer```
 
 In quiz_data.py the function "load_questions" the csv file "question.csv" will be loaded and an empty questions list is created.

 ```python
 def load_questions(filepath='question.csv'): #creating function to load questions from csv file
    questions = [] #empty list to store questions
 ```
  Using a for loop it will loop through each row in the CSV file and add it into the empty list and convert each question into a dictionary with the four ooptions. The answer values in the CSV file are represented as an integer so that pyton can read it by its index. 

  ```python
   for row in reader: #will loop for each row in questions.csv file
            questions.append({ #adding to the empty list
                "questions":row["questions"],
                "options":[
                    row["option1"],
                    row["option2"],
                    row["option3"],
                    row["option4"],
                ],
                "answer":int(row["answer"])-1 #index is always 0 so -1
            })
    return questions
```
In the main.py ile I begin by importing libaries, the csv files, and the testing framework
```python
import tkinter as tk #importing tkinter for GUI
import re # used to check names
from tkinter import messagebox #import messagebox for end of quiz messsage
import csv #import CSV 

from quiz_data import load_questions #import function to get questions

```
Now underneath the code is a character check function that will check if the names inputted have any integer characters within them. I added this once my code was finished to purposely get a unit test fail. It is outside the class as I need the test file to read just that function and not the whole class.
```python
def character_check(name:str) -> bool: # function to check that imputtted names don't have numbers
    return not re.search(r"\d",name)
```
In the main.py file I have built a class. It will first create and design the GUI window.
```python
class Quizzapp(tk.Tk): 
    def __init__(self,questions): #creating window 
        super().__init__()
        self.title("Defect Management quiz")
        self.geometry('600x500')#rectangle sized
        self.configure(bg='#F1D983')#pastel yellow background
```

Here I have created variables that will be throught the app. 
- self.questions will store all the questions from "question.csv"
- self.current_question will start the quiz from question 1 (index=0) and track the question as they are displayed
- self.score is going to calculate the users score starting at zero
- self.name will store the inputted name

```python
self.questions = questions #storing questions
        self.current_question = 0 #will start on first question, index always starts on 0
        self.score = 0
        self.name=tk.StringVar() #stores user's name
        self.answer_var = tk.IntVar(value=-1)
        self.answer_vars = []
```
This section is also designing the GUI. The labels are displaying the questions and feedback, as well as the instruction "Please enter your name in the box". Buttons are used for the four options and and next button that the user will interact with. The name entry field allows the user to input. 

The for loop will loop through the five questions improve the maintainability of code by reducing duplicates and improveing readability.
```python
self.name_label=tk.Label( #creating Name widget 
            self,
            text="Please enter your name in the box below",
            bg="#F1D983",
            fg="black",
            font=("Arial",20)
        )

        self.name_label.pack(pady=10) #packing name and displaying

        self.name_entry = tk.Entry( #Name input box
            self,
            textvariable=self.name,
            font=("Arial",20),
            fg="black",
            bg="#F1D983"
        )

        self.name_entry.pack(pady=10) #packing and displaying

        self.question_label=tk.Label(
            self,
            text="",
            bg="#F1D983",
            font=("Arial",16),
            wraplength=500
        )

        self.question_label.pack(pady=15) #packing and displaying

        self.choice_buttons = []

        for i in range(4):
            button = tk.Button(
                self,
                width=40,
                bg="#F1D983",
                fg="black",
                activebackground="#F1D983",
                relief="flat",
                borderwidth=0,
                command=lambda i=i: self.check_answer(i)
            )
            button.pack(pady=8)
            self.choice_buttons.append(button)

        self.feedback_label = tk.Label(
            self,
            text="",
            bg="#F1D983",
            font=("Arial",14)
        )

        self.feedback_label.pack() #packing and displaying

        self.score_label = tk.Label(
            self,
            text="Score : 0",
            bg="#F1D983",
            font=("Arial",14)
        )
        self.score_label.pack() #packing and displaying

        self.next_button = tk.Button(
            self,
            text="Next",
            command=self.next_question,
            state="disabled"
        )

        self.next_button.pack(pady=10)

```

Near the bottom of the code i have written functions that each have a role in ensure that the code works correct give the correct outputs and 
- show_quesion(self) - shows the cuureent questin and four option buttons, it will also disable the next button until an option is clicked,
- check_answer(self,choice) - will check the chosen option against answers saved from CSV file  and output feedback. I correct answer will so add to the score aswell. 
- next_question(self) - will move onto the next question until each question is shown then it will present an error message and close.
- save_results - will save the name and score in "results.csv" file

```python
def show_questions(self):
        question = self.questions[self.current_question]

        self.question_label.config(
            text=question["questions"]
        )

        for i in range (4): # for loop for the four options
            self.choice_buttons[i].config(
                text=question["options"][i],
                state="normal"
            )

        self.feedback_label.config(text="")
        self.next_button.config(state="disabled") #button is disabled until option is clicked

    def check_answer(self,choice):
        question = self.questions[self.current_question]

        if choice == question["answer"]: #calculating scores
            self.score += 1

            self.score_label.config(
                text=f"Score: {self.score}"
            )

            self.feedback_label.config(
                text="Correct!", #feedback
                fg="green",
            )

        else:
            self.feedback_label.config(
                text="Inorrect!",
                fg="red", #feedback
            )
        self.next_button.config(state="normal") #enables next button from disabled

    def next_question(self):
        self.current_question += 1 #moves to next question
        if self.current_question < len(self.questions):
            self.show_questions()
        else:
           self.save_results()
           messagebox.showinfo("Well done! You completed the quiz!")
           self.destroy() #close application

    def save_results(self): #saving user's name and score to result.csv
        with open("results.csv",mode="a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                 self.name.get(),
                 self.score
            ])
```

# Testing

## Manual testing
Whilst coding I started with manual testing, testing the code was functional.

|Test|Test Data|Expected Result|Actual Result|Status|
|----|---------|---------------|-------------|------|
|Launch app|Run main.py file|GUI window opens successfully|works as expected|Pass|
|Enter valid name|"Natasha"|Name accepted and saved into csv file once quiz is completed|Works as expected|Pass|
|Enter invalid naem|123|Name not accepted and error message pops up|
|recieve red "Incorrect" when answer is wrong|Incorrect option|red "Incorrect" message is shown|Working as exoected|pass|


## automation testing

First I checked that my unit testing framwork was working by assert the value 1 to true which is correct.
```python
import unittest
from quiz_data import load_questions

class TestSmoke(unittest.TestCase):

    def test_load_questions_runs(self):
        self.assertTrue(1)

if __name__=="__main__":
    unittest.main(verbosity=1)
``` 
![proof of unit test 1](image-2.png)
then I add a function that will check that the questions are successfully loading from csv file.
```python
def test_load_questions_runs(self):
    questions=load_questions()
    self.assertIsNotNone(questions)
```
![proof of unit test 2](image-3.png)

then I add character_check functions that will check if the validation of names is correct. This will not work since there is no validation in the main.py file so we should recieve an error

```python
 def test_character_check_happy(self):
        self.assertTrue(character_check("Natasha"))
        self.assertTrue(character_check("Natasha Zinyuke"))

def test_character_check_unhappy(self):
    self.assertFalse(character_check("Natasha001"))
    self.assertFalse(character_check("#Natashaisthenumber1best"))
```
![Proof of unit test 3](image-4.png)

To make this test now work and run correctly I imported re which will check through the inputted names and look for any integers. 
```python
def character_check(name:str) -> bool:
    return not re.search(r"\d",name)
```

Then add an if statemnet at the both of the code which allow it to work successfully.
```python
if __name__=="__main__":
    app = Quizzapp(questions)
    app.mainloop()
```
|Test|Test Type|Test Data|Expected result|Actutal Result|Status|
|----|---------|---------|---------------|--------------|------|
|Test that automated test is working|Smoke test| |Test is with no errors|Working as expected|Pass|
|Check the questions are loaded from the CSV file|Unit test|load_question()|Questions are displayed|Working as expected|Pass|
|check valid names pass|unit test|"Natasha" "Natasha Zinyuke"| function returns True|working as expected|Pass|
check valid names pass|unit test|"Natasha0001" "#Natashaisthenumber1best"| function returns False|working as expected|Pass|

# Documentation

## User Documentation
#### Step 1: Lanuch the application
#### Step 2: Enter your name
#### Step 3: Read questions carefully and click your chosen answer
#### Step 4: Once feedback is recieved click next to move onto the next question
#### Step: Repeat steps 3 and 4 until quiz is complete

## Technical Documentation
To download or save this project to your device run this command in the terminal
```bash
git clone https://github.com/NUnatasha/Defect-management-quiz-summative-two-/blob/main/README.md
```
After clone use this line to move into folder

```bash
cd Defect-managemnet-quiz-summative-two
```
- main.py - File contains the the app functionality, Graphical User Interface (GUI) 
- quiz_data.py - file contains "load_question()" function that loads questions from csv
- results.csv - File contains names and scores of users who have attempted teh quiz
- test_quiz.py - File contains automated unit testing

# Evalution
In conclusion, this project is successful in developing a simple defect management quiz whichh i'm sure will help assess users and teach them on some basic defect concepts. It meets majority of the functional requirements ensuring that the user can successfully use the quiz correctly with the steps guided backs. 

However, some improvements I will make in the future that will make this a stronger and much more useful is adding more complex questions. Adding harder questions will really test users and highlight any areas which require more guidance or clarity. I also believe to really encorage users is to added a leaderboard. Since scores are saved successfully into results.csv a leader can help motivate and create healthy competition that will encourage users to take the time to learn more surrounding defects.

Furthermore, I think adding a date and time by import would improve the score taking so progress can be tracked and checked. I believe this project works well and some improvements could be really beneficial for staff/users