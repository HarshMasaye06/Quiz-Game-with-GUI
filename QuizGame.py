from tkinter import *
from tkinter.ttk import *

root = Tk()

root.geometry('400x190')
root.title("-----!! Question no 1 !!-----")


def select(event):
    b = event.widget
    value = b['text']

    for i in range(15):
        if value == answer_key[i]:
            questionsArea.delete(1.0, END)
            root.title(f"-----!! Question no {i + 2} !!-----")
            questionsArea.insert(END, questions[i + 1])
            optionbtn1.config(text=option1[i + 1])
            optionbtn2.config(text=option2[i + 1])
            optionbtn3.config(text=option3[i + 1])
            optionbtn4.config(text=option4[i + 1])
        if value not in answer_key:
            root.destroy()
            break


def chance50():
    if questionsArea.get(1.0, 'end-1c') == questions[0]:
        optionbtn1.config(text='')
        optionbtn2.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[1]:
        optionbtn1.config(text='')
        optionbtn4.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[2]:
        optionbtn3.config(text='')
        optionbtn4.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[3]:
        optionbtn3.config(text='')
        optionbtn4.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[4]:
        optionbtn1.config(text='')
        optionbtn4.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[5]:
        optionbtn2.config(text='')
        optionbtn4.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[6]:
        optionbtn4.config(text='')
        optionbtn2.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[7]:
        optionbtn4.config(text='')
        optionbtn2.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[8]:
        optionbtn2.config(text='')
        optionbtn4.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[9]:
        optionbtn1.config(text='')
        optionbtn2.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[10]:
        optionbtn1.config(text='')
        optionbtn3.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[11]:
        optionbtn1.config(text='')
        optionbtn3.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[12]:
        optionbtn3.config(text='')
        optionbtn2.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[13]:
        optionbtn3.config(text='')
        optionbtn2.config(text='')
        lifeline50.config(state=DISABLED)
    if questionsArea.get(1.0, 'end-1c') == questions[14]:
        optionbtn1.config(text='')
        optionbtn3.config(text='')
        lifeline50.config(state=DISABLED)


def expertadvice():
    if questionsArea.get(1.0, 'end-1c') == questions[0]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[0])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[1]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[1])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[2]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[2])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[3]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[3])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[4]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[4])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[5]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[5])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[6]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[6])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[7]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[7])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[8]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[8])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[9]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[9])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[10]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[10])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[11]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[11])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[12]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[12])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[13]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[13])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()
    if questionsArea.get(1.0, 'end-1c') == questions[14]:
        root1 = Tk()
        answer = Label(root1, text=answer_key[14])
        lifelineExpertAdvice.config(state=DISABLED)
        answer.pack()
        root1.mainloop()


questions = ["Which is the largest country in the world?",
             "How many days are there in a leap year?",
             "Which one of these four birds has the longest beak and feet?",
             "What is the national currency of the United States of America (USA)?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

option1 = ["India", "354",
           "Heron", "Euro",
           "Javascript", "36",
           "Windows 7", "Elephant", "11:23PM", "KKR",
           "Earth", "8",
           "100 years", "Google", "Monty Ritz"]

option2 = ["USA", "366",
           "Parrot", "Peso ",
           "Python", "34",
           "Linux", "Lion", "11.11PM", "CSK",
           "Uranus", "5",
           "50 years",
           "Microsoft", "Danis Lio"]

option3 = ["China", "365",
           "Crow", "Dollar",
           "Java", "30",
           "Mac", "Tiger", "7:23PM", "MI",
           "Mars", "7",
           "500 years",
           "Amazon", "Bill Gates"]

option4 = ["Russia", "420",
           "Pigeon", "Yen",
           "C++", "37",
           "Windows XP", "Cow", "9.11PM", "RCB",
           "Jupiter",
           "6",
           "1000 years", "Apple",
           "Jeff Bezos"]

answer_key = ["Russia", "366", "Heron", "Dollar", "Python", "36",
              "Linux", "Lion", "11:23PM", "MI", "Jupiter", "7", "1000 years", "Apple",
              "Bill Gates"]

welcome = Label(root, text="!! Welcome to Quiz Game !!")
welcome.grid(row=0, columnspan=2)

questionsArea = Text(root, width=50, height=3)
questionsArea.grid(row=1, columnspan=2)
questionsArea.insert(END, questions[0])

options = Label(root, text="Options")
options.grid(row=2, columnspan=3)
optionbtn1 = Button(root, text=option1[0])
optionbtn1.grid(row=3, column=0)
optionbtn2 = Button(root, text=option2[0])
optionbtn2.grid(row=3, column=1)
optionbtn3 = Button(root, text=option3[0])
optionbtn3.grid(row=4, column=0)
optionbtn4 = Button(root, text=option4[0])
optionbtn4.grid(row=4, column=1)

optionbtn1.bind("<Button-1>", select)
optionbtn2.bind("<Button-1>", select)
optionbtn3.bind("<Button-1>", select)
optionbtn4.bind("<Button-1>", select)

lifeline = Label(root, text="LifeLines")
lifeline.grid(row=5, columnspan=3)

lifeline50 = Button(root, text="50-50", command=chance50)
lifeline50.grid(row=6, column=0)

lifelineExpertAdvice = Button(root, text="Expert Advice", command=expertadvice)
lifelineExpertAdvice.grid(row=6, column=1)


root.mainloop()
