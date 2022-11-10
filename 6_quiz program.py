quiz={
    "qustion1":{
        "question":"what is the capital of france?",
        "answer":"paris"
    },
    "question2":{
        "question":"what is the full form ml?",
        "answer":"machine learning"
    },
    "question3":{
        "question":"what is the full form AI?",
        "answer":"artificial intelligence"
    },
    "question4":{
        "question":"what is the state of pune?",
        "answer":"maharashtra"
    },
    "question5":{
        "question":"what is the python?",
        "answer":"high level programming language"
    },
    "question6":{
        "question":"full form of gui?",
        "answer":"graphical user interface"
    },
    "question5":{
        "question":"full form of mvc?",
        "answer":"micro view controller"
    }
}

score=0

for key,value in quiz.items():
    print(value['question'])
    answer=input("answer:")

    if answer.lower() == value["answer"].lower():
        print("correct")
        score = score + 1
        print("your score is: " + str(score))

    else:
        print("incorrect!")
        print("the answer is: " + value['answer'])
        print("your score is: " + str(score))
        print("")
        print("")

print("you got "  + str(score) + "out of 7 question correctly")
print("your percentage is " + str(int(score/7*100)) + "%")