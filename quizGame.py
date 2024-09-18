# Python quiz game

questions = ("How many elements are in the periodic table?: ",
            "Which animalays the largest eggs?: ",
            "What is the most abundant gas in Eath's atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system is the hottest?: ",
            "Which is the largest ocean on Earth?: ",
            "What is the smallest unit of matter?: ",
            "What is the chemical symbol for gold?: ",
            "Which organ in the human body is responsible for filtering blood?: ",
            "Who developed the theory of general relativity?: "
            )

options = (("A. 116", "B. 117", "C. 118", "D. 119"), 
           ("A. Whale", "B. Crocoddile", "C. Elephant", "D. Ostrich"), 
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
           ("A. 206", "B. 207", "C. 208", "D. 209"), 
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
           ("A. Atom", "B. Molecule", "C. Proton", "D. Electron"),
           ("A. Au", "B. Ag", "C. Pb", "D. Fe"),
           ("A. Liver", "B. Kidney", "C. Heart", "D. Lungs"),
           ("A. Isaac Newton", "B. Galileo Galilei", "C. Albert Einstein", "D. Nikola Tesla"))

answers = ("C", "D", "A", "A", "B", "D", "A", "A", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper()
        
    while not guess.upper() in answers:
        guess = input("Enter (A, B, C, D): ").upper()
    else:
        guesses.append(guess)
        
    if guess == answers[question_num]:
        score += 1
        print("Correct 😀")
    else:
        print("Incorrect 🥺")
        print(f"{answers[question_num]} is the correct answer.")
        
    question_num += 1
    
print("---------------")
print("    Results    ")
print("---------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
if score == 100:
    print(f"Your score is: {score}% 🍾🥂🎉")
elif score >= 60:
    print(f"Your score is: {score}% 😀")
else:
    print(f"Your score is: {score}% 🥺. Try it again.")