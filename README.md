# Defect-management-quiz
this is my summative two code for IFCP course, year one

## Order of Documentation
1. Introduction
2. Design
3. Development
4. Testing
5. User Documentation
6. Technical Documentation
7. Evaluation 

# Introduction
As new websites, apps and software system are becoming increasingly important to business operations so does the quality. It is important that these applications are efficient, reliable and provide great customer sattisfaction. 

The Software Development Life Cycle (SDLC) includes the important part of testing and defect managemnmet plays a key role in that. As you perform functional testing, regression testing, unit testing, system testing and User Acceptance Testing (UAT) bugs and defects are going to found. Defect managemnet can ensure that these bugs/defects are identified correctly, tracked and auditted properly, prioritised during testing. Making sure that the relevant employees have a strong understanding and knowledge around this proccess can help reduce failures, improve quality of software and have effective collaboration for the resolution

This project is a simple multiple choice quiz using python(https://www.python.org) and Tkinter (). The purpose of this quiz application is to test the user on their knowledge on defect Management and to provide training. Five qustions multiple choice questions are displayed one at a time allow the user to select one option out of four.

# Design 

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

# Developnent
## technologies used
1. Python
2. Tkinter
3. CSV module

## Project Structure
 hehrheeuj

The questions are stored in a CSV file which is pulled and loaded into python using a function called load_questions. Within the function the csv file "question.csv" will be loaded and an empty questions list is created. Using a for loop it will loop through each row in the CSV file and add it into the empty list and convert each question into a dictionary with the four ooptions. The answer values in the CSV file are represented as an integer so that pyton can read it by its index. 

CSV structure: questions,option1,option2,option3,option4,answer
# Testing

## Manual testing

# Technical Documentation

# User Documentation

# Evalution
- add date and time to show date of when user takes quiz
- adding more complex quix 
- adding levels depending on users confidence
- leaderboard to encourage people to take the quiz
