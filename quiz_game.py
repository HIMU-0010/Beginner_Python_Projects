questions = ("Which programming language is commonly used for artificial intelligence and machine learning applications?", 
             "What is the name of the protocol used to transfer web pages from a web server to a browser?",
             "Which company developed the Android operating system?",
             "What is the term for the unique address assigned to each computer connected to the internet?",
             "In Morse code, which letter is represented by a single dot?")

options = (("A. Python", "B. Java", "C. Ruby", "D. C++"),
           ("A. TCP/IP", "B. FTP", "C. HTTP", "D. SMTP"), 
           ("A. IBM", "B. Microsoft", "C. Apple", "D. Google"),
           ("A. MAC address", "B. IP address", "C. URL", "D. DNS"),
           ("A. E", "B. A", "C. G", "D. Q"))

answers = ("A", "C", "D", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!!")
    else:
        print("Incorrect!!!")
    question_num += 1


print("---------------------")
print("       RESULT        ")
print("---------------------")

print("Answers: ", end="")
for answer in answers:
    print(f"{answer}", end=" ")

print()
print("Guesses: ", end="")
for guess in guesses:
    print(f"{guess}", end=" ")

score = int(score / len(questions) * 100)
print()
print(f"Your score is {score}%")
