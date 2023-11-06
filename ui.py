from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz:QuizBrain):
          self.quiz=quiz
          self.window=Tk()
          self.window.title("Quizler")
          self.window.config(bg=THEME_COLOR,padx=20,pady=20)

          self.score=Label(text="SCORES: 0",bg=THEME_COLOR,fg="white")
          self.score.grid(row=0,column=1)

          
          self.canvas=Canvas(width=300,height=258,bg="white")
          self.qt=self.canvas.create_text(150,125,width=280,text="HELLO",fill=THEME_COLOR,font=("Arial",20,"italic"))
          self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

          tick_image=PhotoImage(file="images/true.png")
          cross_image=PhotoImage(file="images/false.png")
          self.tick=Button(image=tick_image,command=self.user_answer_true)
          self.cross=Button(image=cross_image,command=self.user_answer_false)
          self.tick.grid(column=0,row=2)
          self.cross.grid(column=1,row=2)
          
          self.get_next_question()
          self.window.mainloop()
          
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.qt,text=q_text)
        else:
            self.canvas. itemconfig(self.qt,text="You have reached the end of quiz") 
            self.tick.config(state="disabled") 
            self.cross.config(state="disabled") 
    def user_answer_true(self):
        user_answer="True"
        is_right=self.quiz.check_answer(user_answer)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")   
        self.window.after(1000,self.get_next_question)     
        
        

    def user_answer_false(self):
        user_answer="False"
        is_right=self.quiz.check_answer(user_answer)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")   
        self.window.after(1000,self.get_next_question)  

        