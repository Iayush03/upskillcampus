# Quiz Game

questions = [
    {
        "question": "Python kis type ki language hai?",
        "options": ["A. Low-level", "B. High-level", "C. Machine", "D. Assembly"],
        "answer": "B"
    },
    {
        "question": "HTML ka full form kya hai?",
        "options": ["A. Hyper Trainer Marking Language", "B. Hyper Text Markup Language", "C. Hyper Text Marketing Language", "D. None"],
        "answer": "B"
    },
    {
        "question": "CSS ka use kis liye hota hai?",
        "options": ["A. Styling", "B. Programming", "C. Database", "D. Security"],
        "answer": "A"
    }
]

score = 0

print("🎮 Welcome to Quiz Game!\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!\n")

print("🎉 Quiz Finished!")
print("Your Score:", score, "/", len(questions))