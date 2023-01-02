print("Welcome to quiz game!")

want_play = input("Do you want to play? ")

if want_play.lower() != "yes":
    quit()

questions_answers = [["What does CPU stand for? ", "central processing unit"], ["What does GPU stand for? ", "graphics processing unit"], ["What does RAM stand for? ", "random access memory"], ["What does PSU stand for? ", "power supply unit"]]

score = 0

for question_answer in questions_answers:
    
    answer = input(question_answer[0])
    
    if answer.lower() == question_answer[1]:
        score += 1 # score = score + 1
        print("Correct!")
    else: 
        print("Incorrect!")
        
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%")