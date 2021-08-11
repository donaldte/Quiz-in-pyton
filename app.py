from class_app import Question

Question_to_answer=[
	'Who is the president of Cameroon?\n(a) Paul Biya\n(b) Tedom Donald\n(c)Maurice Kamto\n\n',
	'What this the Capital of Cameroon?\n(a) Douala\n(b) Bafoussam\n(c)Yaounde\n\n',
	'what is the name of the big football player of Cameroon ?\n(a) Sammuel Etoo\n(b) Tedom Donald\n(c) Son\n\n',


]

Array_of_response_and_question = [
	Question(Question_to_answer[0], 'a'),
	Question(Question_to_answer[1], 'c'),
	Question(Question_to_answer[2], 'a'),
]

def run_test(questions):
    print("\t\t\t\t||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("\t\t\t\t||                   Welcome to Question Quiz                 ||")
    print("\t\t\t\t||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\n")
    name = input("Hello , Please Enter your Name: ")
    print("Thank You can start Now\n\n")
    score=0
    for question in questions:
    	print(question.question)
    	answer = input("write your correct answer: ")
    	if answer == question.anwser :
    		score+=1
    if score==3:			
    	print(f"\t\t\t\tHey {name} you got {score}/{len(questions)} Excellent!!")
    elif score==2:			
    	print(f"\t\t\t\tHey {name} you got {score}/{len(questions)} Good!!")
    else:		
    	print(f"\t\t\t\tHey {name} you got {score}/{len(questions)} poor!!")
    again = input("Do you want to play again? (yes/no)")
    if again == 'yes':
    	run_test(Array_of_response_and_question)
    else:
    	exit()			
run_test(Array_of_response_and_question)			
