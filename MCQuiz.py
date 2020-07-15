from Question import Question

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt 
        self.answer = answer 
     
question_promps = [ 
    "What is Magnus Carlson's full name?\n(a) Sven Magnus Øen Carlsen\n(b) Magnus Bjørn Carlsen\n(c) Håvard Magnus Øystein Carlsen\n\n"
    "What is Kasparov's favorite chess opening with the black peices?\n(a) Sicilian Defense: Scheveningen\n(b) King’s Indian Defence, Samisch\n(c) Gruenfeld Defense\n\n"
    "How long was Fischer world champion before he forfited his title to Karpov?\n(a) 5 years\n(b) 3 years\n(c) 2 years\n\n"
]

questions = [ 
    Question(question_promps[0], "a"),
    Question(question_promps[0], "c"),
    Question(question_promps[0], "b"),
]

def run_test(questions): 
    score = 0 
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1 
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct.") 

run_test(questions)
