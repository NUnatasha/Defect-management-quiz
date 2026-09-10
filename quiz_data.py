import csv #import csv module so it can read from questions.csv file

def load_questions(filepath='questions.csv'): #creating function to load questions from csv file
    questions = [] #empty list to store questions

    with open(filepath,newline='',encoding='utf=8') as csvfile:
        reader = csv.DictReader(csvfile)
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