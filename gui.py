from tkinter import *
from question_brain import QuizBrain
THEME_COLOR = "#375362"
initial_time = 30
flag = TRUE


class graphics:
    def __init__(self,quiz_brain: QuizBrain):
        self.time = initial_time
        self.flag = flag

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx = 50, pady = 50, bg= THEME_COLOR)

        self.score_label = Label(text="  Score : 0", fg="white", bg=THEME_COLOR, font=("Arieal", 20, "bold"))
        self.score_label.grid(row=0,column=2)


        self.time_label = Label(text="Time: 00:00", fg="white", bg=THEME_COLOR, font=("Arieal", 20, "bold"))
        self.time_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Quiz", fill=THEME_COLOR, font=("Arial", 20) )
        self.canvas.grid(row=1, column=0, columnspan=3)
        

        self.true_pic = PhotoImage(file= "Images/true.png")
        self.false_pic = PhotoImage(file= "Images/false.png")
        self.true_button = Button(image = self.true_pic, highlightthickness=0, command = self.true_pressed)
        self.true_button.grid(row=2, column=1)
        self.false_button = Button(image = self.false_pic, highlightthickness=0, command = self.false_pressed)
        self.false_button.grid(row=2, column=2)


        self.count_down(self.time)
        self.get_next_question()

        
        self.window.mainloop()



    def get_next_question(self):
        global initial_time
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions_left():
            self.score_label.config(text=f"  Score: {self.quiz.score}/{len(self.quiz.questionbank)}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.after(1000, self.correction)
            self.flag = False
            

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
            if is_right:
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)

    def correction(self):
        if self.quiz.score >= 10:
            self.canvas.itemconfig(self.question_text, text="You've passed")
        else:
            self.canvas.itemconfig(self.question_text, text="You've failed")

    
    def count_down(self,time):
        if self.flag:
            if time >= 0:  
                self.time_label.config(text= f"00:{"%02d" % time}")
                self.window.after(1000, self.count_down, time-1)
        else:       
            self.time_label.config(text= "00:00")
