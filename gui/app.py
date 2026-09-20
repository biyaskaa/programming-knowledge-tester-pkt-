import tkinter as tk
from pathlib import Path

from core.storage import load_questions
from gui.start_frame import StartFrame
from gui.quiz_frame import QuizFrame
from gui.result_frame import ResultFrame

import sys
import os

def resource_path(relative_path):
    """Возвращает путь к файлу, работающий и в обычном режиме, и в PyInstaller."""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Programming Knowledge Tester")
        self.geometry("700x450")

        self.questions_path = resource_path("data/questions.json")
        self.all_questions = load_questions(self.questions_path, enc="utf-8")

        # место, где будет храниться текущая сессия Quiz
        self.quiz = None

        # контейнер, в котором лежат все фреймы друг на друге
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartFrame, QuizFrame, ResultFrame):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartFrame")

    def show_frame(self, name):
        self.frames[name].tkraise()