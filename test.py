def cbt():
    questions = [
        {"question":"What is 2 + 2?\n (a) 3\n (b) 4\n (c) 5\n (d) 6", "answer":"b"},
        {"question":"What color is the sky on a clear day?\n (a) Red\n (b) Blue\n (c) Green\n (d) Yellow", "answer":"b"},
        {"question":"How many legs does a spider have?\n (a) 6\n (b) 7\n (c) 8\n (d) 9", "answer":"c"},
        {"question":"Python is a programming language. (True/False)", "answer":"true"},
        {"question":"What is 5 * 6?\n (a) 11\n (b) 30\n (c) 56\n (d) 25", "answer":"b"}
    ]
    
    score = 0
    for q in questions:
        print(q["question"])
        answer = input("Your answer: ").strip().lower()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print("❌ Wrong!\n")

    print(f"Your final score is {score}/{len(questions)}")
cbt()