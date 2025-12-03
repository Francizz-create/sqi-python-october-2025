# Project Overview:
# Develop a simple Computer-Based Testing (CBT) program in Python that hardcodes a set of 
# at least 5 objective questions and their answers. The program should ask these questions 
# to the user one by one and display the user's score at the end.

# Requirements:
# 1. Hardcode Questions and Answers:
# Create at least 5 objective questions (multiple choice or true/false).
# Hardcode these questions and their correct answers in your program.
#2.  Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# 3. Scoring System:
# Compare the user's answers with the correct answers.
# Keep track of the user's score.
# 4. Display Results:
# At the end of the quiz, display the user's total score.


def cbt():
    questions = [
        {
            "question":"What is 2 + 2?\n (a) 3\n (b) 4\n (c) 5\n (d) 6",
            "answer":"b"
        },
        {
            "question":"What color is the sky on a clear day?\n (a) Red\n (b)Blue\n (c)Green\n (d)Yellow",
            "answer":"b"

        },
        {

            "question":"How many legs does a spider have?\n (a) 6\n (b) 7\n (c)8\n (d) 9",
            "answer": "c"
        },
        {
            "question": "2. Python is a programming language. (True/False)",
            "answer": "true"
        },
        {
            "question": "4. What is 5 * 6?\n(a) 11\n(b) 30\n(c) 56\n(d) 25",
            "answer": "b"
        }
        ]
    # cbt(questions)
    
    score = 0
    for i in questions:
        print(i["question"])
        answer = input("Your answer: ").strip().lower()

        if answer == i["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!\n")

    # final score
    print(f"Your final score is {score}/{len(questions)}")

cbt()


# Project Overview:
# Develop an Exam Wizard program in Python that hardcodes a set of at least 5 theory 
# questions and evaluates the student's answers based on the presence of specific keywords or phrases. 
# The program should ask these questions to the user one by one and display the user's score at the end.

# Requirements:
# 1.Hardcode Questions and Keywords:
# Create at least 5 theory questions.
# For each question, determine the essential keywords or phrases that should be included in the ideal answer.
# Assign weights to each keyword based on its importance.

# 2.Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.

# 3.Scoring System:
# Evaluate the user's answers based on the presence of the specified keywords..
# Keep track of the user's score.

# 4.Display Results:
# At the end of the quiz, display the user's total score out of the max score e.


questions = [
        {
            "question": "Explain the process of photosynthesis.",
            "keywords": {"Photosynthesis":2, "Light energy":1, "Chemical energy": 1, "Chloroplasts":2,  "Chlorophyll": 1, 
            "Carbon dioxide":1, "Water": 1, "Glucose": 1, "Oxygen": 1, "ATP": 1,}
        },
        
        {
            "question": "2. What are the main features of Object-Oriented Programming (OOP)?",
            "keywords": {"encapsulation": 2, "inheritance": 2, "polymorphism": 2, "abstraction": 2}
        },
        {
            "question": "3. Describe the water cycle.",
            "keywords": {"evaporation": 2, "condensation": 2, "precipitation": 2, "collection": 1}
        },
        {
            "question": "4. What are the advantages of using Python?",
            "keywords": {"easy": 1, "readable": 1, "libraries": 2, "community": 1, "cross-platform": 2}
        },
        {
            "question": "5. Explain the importance of the Internet in modern society.",
            "keywords": {"communication": 2, "information": 2, "education": 1, "business": 2, "globalization": 2}
        }
    ]
    
total_score = 0
max_score = sum(sum(i["keywords"].values()) for i in questions)
    
for i in questions:
    print(i["question"])
    answer = input("Your answer: ").lower()

# Evaluating based on keywords
question_score = 0
for keyword, weight in i["keywords"].items():
    if keyword in answer:
        question_score += weight

    # total_score += question_score

# final results
print("=== Exam Results ===")
print(f"Your total score: {total_score}/{max_score}")


