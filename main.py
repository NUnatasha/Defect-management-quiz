import tkinter as tk
from tkinter import messagebox
import csv

from quiz_data import load_questions #import function to get questions

questions = load_questions()

class Quizzapp(tk.Tk): 
    def __init__(self,questions): #creating window 
        super().__init__()
        self.title("Defect Management quiz")
        self.geometry('600x500')
        self.configure(bg='#F1D983')

        self.questions = questions #storing questions
        self.current_question = 0 #will start on first question, index always starts on 0
        self.score = 0
        self.name=tk.StringVar() #stores user's name
        self.answer_var = tk.IntVar(value=-1)
        self.answer_vars = []

        self.name_label=tk.Label( #creating Name widget 
            self,
            text="Please enter your name in the box below",
            bg="#F1D983",
            fg="black",
            font=("Arial",20)
        )

        self.name_label.pack(pady=10)# packing name and displaying

        self.name_entry = tk.Entry(
            self,
            textvariable=self.name,
            font=("Arial",20),
            fg="black",
            bg="#F1D983"
        )

        self.name_entry.pack(pady=10)

        self.question_label=tk.Label(
            self,
            text="",
            bg="#F1D983",
            font=("Arial",16),
            wraplength=500
        )

        self.question_label.pack(pady=15)

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

        self.feedback_label.pack()

        self.score_label = tk.Label(
            self,
            text="Score : 0",
            bg="#F1D983",
            font=("Arial",14)
        )
        self.score_label.pack()

        self.next_button = tk.Button(
            self,
            text="Next",
            command=self.next_question,
            state="disabled"
        )

        self.next_button.pack(pady=10)

        self.show_questions()

    def show_questions(self):
        question = self.questions[self.current_question]

        self.question_label.config(
            text=question["questions"]
        )

        for i in range (4):
            self.choice_buttons[i].config(
                text=question["options"][i],
                state="normal"
            )

        self.feedback_label.config(text="")
        self.next_button.config(state="disabled")

    def check_answer(self,choice):
        question = self.questions[self.current_question]

        if choice == question["answer"]:
            self.score += 1

            self.score_label.config(
                text=f"Score: {self.score}"
            )

            self.feedback_label.config(
                text="Correct!",
                fg="green",
            )

        else:
            self.feedback_label.config(
                text="Inorrect!",
                fg="red",
            )
        self.next_button.config(state="normal")

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_questions()
        else:
           self.save_results()
           messagebox.showinfo("Well done! You completed the quiz!")
           self.destroy()

    def save_results(self):
        with open("results.csv",mode="a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                 self.name.get(),
                 self.score
            ])

app = Quizzapp(questions)
app.mainloop()