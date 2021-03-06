#Defining variables
user_answerConfirm = str
user_answer = str
user_score = 0
ans_check = True
ans_checkConfirm = True
end = True
x = 0
y = 0

#Assigning questions and answers to each position in the list
question1 = ("""Who was the Greek or Roman God of War?
1. Ares
2. Athena
3. Zues
4. Apollo""")
question1_correct = 1
question1_userAnswer = str

Q1 = [question1,question1_userAnswer,question1_correct]

question2 = ("""What chemical element is diamond made of?
1. Silicon
2. Argon
3. Carbon
4. Boron""")
question2_correct = 3
question2_userAnswer = str

Q2 = [question2,question2_userAnswer,question2_correct]

question3 = ("""What is the name of the poker hand containing three of a kind and a pair?
1. Royal Flush
2. Full House
3. Three of a Kind
4. Two Pair""")
question3_correct = 2
question3_userAnswer = str

Q3 = [question3,question3_userAnswer,question3_correct]

question4 = ("""What part of the body produces insulin?
1. Pancreas
2. Kidney
3. Brain
4. Liver""")
question4_correct = 1
question4_userAnswer = str

Q4 = [question4,question4_userAnswer,question4_correct]

question5 = ("""In a standard pack of cards, which king is the only one to not have a moustache?
1. King of Spades
2. King of Clubs
3. King of Hearts
4. King of Diamonds""")
question5_correct = 3
question5_userAnswer = str

Q5 = [question5,question5_userAnswer,question5_correct]

question6 = ("""How many syllables make up a haiku?
1. 5
2. 7
3. 14
4. 17""")
question6_correct = 4
question6_userAnswer = str

Q6 = [question6,question6_userAnswer,question6_correct]

question7 = ("""What is the standard unit of distance in the metric system?
1. Meter
2. Inches
3. Planck length
4. Kilometers""")
question7_correct = 1
question7_userAnswer = str

Q7 = [question7,question7_userAnswer,question7_correct]

question8 = ("""What is the official language of Brazil?
1. English
2. Spanish
3. Portuguese
4. French""")
question8_correct = 3
question8_userAnswer = str

Q8 = [question8,question8_userAnswer,question8_correct]

question9 = ("""What superhero has been played by Michael Keaton, Val Kilmer, George Clooney and Christian Bale?
1. Superman
2. Captian America
3. Spider-Man
4. Batman""")
question9_correct = 4
question9_userAnswer = str

Q9 = [question9,question9_userAnswer,question9_correct]

question10 = ("""Does 2 + 2 = 5?
1. Yes
2. If you squint really hard
3. 1984
4. idk""")
question10_correct = 3
question10_userAnswer = str

Q10 = [question10,question10_userAnswer,question10_correct]

quiz = [Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10]

#Defining the function being used to ask the questions
def question_Confirm():
    #Making the vars in function global
    global ans_check
    global ans_checkConfirm
    global user_answer
    global user_answerConfirm
    global x
    global end
    while end: #Setting up loop
        ans_checkConfirm = False

        #Asks the user to answer
        print(str(quiz[x][0]))
        print("Enter your answer without anything else.")
        quiz[x][1] = input()
        #Checks if answer given is valid or not
        if ans_check == True:
            try:
                user_answer = int(quiz[x][1])
                if  1 <= user_answer <= 4:
                    ans_check = False
                    ans_checkConfirm = True
                else:
                    print("Please only enter 1, 2, 3, or 4 as viable answers.")
            except ValueError:
                print("You answer was a string.")
                print("Please only enter 1, 2, 3, or 4 as viable answers.")
                ans_checkConfirm = False
            
        if ans_checkConfirm == True:        
            #Asks the user to answer confirmation question.
            print("Confirm that your answer is ", quiz[x][1], " by entering you answer again.")
            user_answerConfirm = input()
            try:
                user_answerConfirm = int(user_answerConfirm)
                if user_answer == user_answerConfirm:
                    ans_checkConfirm = False
                    quiz[x][1] = int(quiz[x][1])
                else:
                    print("Your original answer and confirmed answer dosn't match.")
                    print("Returning you to the original question.")
                    ans_check = True
                
            #If the program sees a string in user_answer the while loop outputs these lines.
            except ValueError:
                print("You answer was a string.")
                print("Please only enter 1, 2, 3, or 4 as viable answers.")
                ans_check = True
        #This makes sure the quiz moves on to the next question
        if ans_check == False and ans_checkConfirm == False:
            ans_check = True
            ans_checkConfirm = True
            x += 1

            #When reaching the end of the quiz end the while loop
            if x > 9:
                end = False
            

def question_Grade():
    #Sets the two booleans to be true so the while loop in question_Confirm can run again
    global y
    global user_score
    ans_check = True
    ans_checkConfirm = True
    #This for loop grades the user's quiz
    for y in range(9):
        if quiz[y][1] == quiz[y][2]:
            user_score += 1
    print("You got ",user_score," out of 10 correct")
        

        


    
