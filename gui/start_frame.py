import tkinter as tk
from tkinter import ttk
from random import sample

from core.quiz import Quiz


class StartFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        title = tk.Label(self, text="Выбери тему и количество вопросов",
                         font=("Arial", 14))
        title.pack(pady=20)

        # выбор темы
        tk.Label(self, text="Тема:").pack()
        self.topic_var = tk.StringVar()
        topics = list(controller.all_questions.keys())
        self.topic_combo = ttk.Combobox(self, values=topics,
                                        textvariable=self.topic_var,
                                        state="readonly")
        self.topic_combo.current(0)
        self.topic_combo.pack(pady=5)

        # выбор количества
        tk.Label(self, text="Сколько вопросов:").pack()
        self.count_var = tk.IntVar(value=5)
        tk.Spinbox(self, from_=1, to=20,
                   textvariable=self.count_var, width=5).pack(pady=5)

        # кнопка старта
        tk.Button(self, text="Начать", command=self.start_quiz,
                  width=15).pack(pady=20)

    def start_quiz(self):
        topic = self.topic_var.get()
        count = self.count_var.get()
        pool = self.controller.all_questions[topic]

        # на случай, если вопросов меньше, чем просили
        count = min(count, len(pool))
        questions = sample(pool, count)

        self.controller.quiz = Quiz(questions)
        self.controller.show_frame("QuizFrame")