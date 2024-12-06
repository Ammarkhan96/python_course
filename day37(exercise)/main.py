questions = [
    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],
    
    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],
    
    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],

    [
        "Which language was used to create fb?", "Python", "Frebch", "JavaScript", "Php", "None", 4
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

money = 0 

# Iterate over the range of levels instead of questions
for i in range(len(levels)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"a. {question[1]}                               b. {question[2]}")
    print(f"c. {question[3]}                               d. {question[4]}")
    reply = int(input("Enter your answer (1-4): "))
    if reply == question[-1]:
        print(f"Correct answer, you have won Rs. {levels[i]}")
        money = levels[i]
    else:
        print("Wrong answer!")
        break  # Exit the loop if the answer is wrong

print(f"Your take home money is Rs. {money}")