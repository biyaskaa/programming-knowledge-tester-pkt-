import tkinter as tk


class ResultFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.result_var = tk.StringVar()
        tk.Label(self, textvariable=self.result_var,
                 font=("Arial", 16)).pack(pady=40)

        tk.Button(self, text="Пройти ещё раз",
                  command=lambda: controller.show_frame("StartFrame"),
                  width=20).pack(pady=10)

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        quiz = self.controller.quiz
        if quiz is not None:
            correct, total = quiz.score()
            self.result_var.set(f"Правильных ответов: {correct} из {total}")