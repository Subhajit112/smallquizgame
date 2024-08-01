from tkinter import *
from gui import graphics
from question_data import question_bank
from question_brain import QuizBrain



quiz = QuizBrain(question_bank)
quiz_ui = graphics(quiz)