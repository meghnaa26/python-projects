questions = ["How many letters are there in a word'Yellow'?","what is 1 + 4?","How many days are in a weeK?","How many hours in a day?","Mountains or beaches?"]
answers = ['6','5','7','24','mountains']
score = 0
for i in range(len(questions)):
    print(questions[i])
    attempts = 4
    while attempts > 0:
        ans = input("Enter the answer: ").lower()
        if answers[i] == ans:
            print("Correct!")
            score += 1
            break
        else:
            attempts -= 1  
            if attempts > 0:
                print("Wrong! Try again, you have", attempts, "chance(s) left")
            else:
                print("Wrong! The right answer is", answers[i])
print("The final score is",score)
