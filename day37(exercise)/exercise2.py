questions = [
    {
        "question": "Which language was used to create Facebook?",
        "options": ["Python", "French", "JavaScript", "PHP"],
        "correct": 4
    },
    {
        "question": "Which is the largest planet in our Solar System?",
        "options": ["Earth", "Jupiter", "Mars", "Saturn"],
        "correct": 2
    },
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Chennai", "Kolkata"],
        "correct": 1
    },
    {
        "question": "Who wrote the Harry Potter series?",
        "options": ["J.R.R. Tolkien", "J.K. Rowling", "George R.R. Martin", "C.S. Lewis"],
        "correct": 2
    },
    {
        "question": "Which part of the plant conducts photosynthesis?",
        "options": ["Root", "Stem", "Leaf", "Flower"],
        "correct": 3
    }
]

# Prize money for each question
prizes = [1000, 5000, 10000, 50000, 100000]

# Game start
print("Welcome to Kaun Banega Crorepati!\n")

money = 0  # Initial prize money

for i in range(len(questions)):
    # Display the question and options
    print(f"Question for Rs. {prizes[i]}:")
    print(questions[i]["question"])
    for j, option in enumerate(questions[i]["options"], start=1):
        print(f"{j}. {option}")

    # Get user's answer
    try:
        answer = int(input("Enter your answer (1-4): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        break

    if answer == questions[i]["correct"]:
        print(f"Correct! You have won Rs. {prizes[i]}.\n")
        money = prizes[i]  # Update the prize money
    else:
        print("Wrong answer! The game is over.")
        break  # End the game if the answer is wrong

print(f"Your take-home money is Rs. {money}. Thank you for playing!")
