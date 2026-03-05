# AI Mock Interview Agent – 5 Questions
from difflib import SequenceMatcher

# Function to calculate similarity
def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

# List of 5 questions with expected answers
questions = [
    {
        "question": "What is Machine Learning?",
        "answer": "Machine learning is a technique where computers learn from data"
    },
    {
        "question": "What is supervised learning?",
        "answer": "Supervised learning uses labeled training data"
    },
    {
        "question": "What is NLP?",
        "answer": "Natural language processing helps computers understand human language"
    },
    {
        "question": "What is an AI agent?",
        "answer": "An AI agent perceives the environment and takes actions to achieve goals"
    },
    {
        "question": "What is RAG in AI?",
        "answer": "RAG is retrieval augmented generation that fetches information and generates answers"
    }
]

print("===== AI Mock Interview Agent =====\n")

score = 0

# Loop through each question
for i, q in enumerate(questions, start=1):
    print(f"Question {i}: {q['question']}")
    user_answer = input("Your answer: ")

    sim = similarity(user_answer, q["answer"])

    if sim >= 0.5:
        print("Feedback: Good answer\n")
        score += 1
    else:
        print("Feedback: Needs improvement\n")

# Final score
print("-----------------------------------")
print(f"Final Score: {score} / {len(questions)}")
print("Interview completed successfully.")
