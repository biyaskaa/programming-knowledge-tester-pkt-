import tkinter as tk


class QuizFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # заголовок "Вопрос X из Y"
        self.progress_var = tk.StringVar()
        tk.Label(self, textvariable=self.progress_var,
                 font=("Arial", 11)).pack(pady=10)

        # текст вопроса
        self.question_var = tk.StringVar()
        tk.Label(self, textvariable=self.question_var,
                 wraplength=600, justify="left",
                 font=("Arial", 13)).pack(pady=15, padx=20)

        # переменная для выбранного варианта
        self.choice = tk.IntVar(value=-1)

        # список радиокнопок (создаём один раз, потом меняем текст)
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self, text="", variable=self.choice,
                                value=i, anchor="w", justify="left")
            rb.pack(fill="x", padx=40, pady=2)
            self.radio_buttons.append(rb)

        # кнопка "Ответить"
        tk.Button(self, text="Ответить", command=self.submit,
                  width=15).pack(pady=20)

    def tkraise(self, *args, **kwargs):
        # при каждом показе этого фрейма — загружаем текущий вопрос
        super().tkraise(*args, **kwargs)
        self.load_question()

    def load_question(self):
        quiz = self.controller.quiz
        if quiz is None or quiz.is_finished():
            return

        q = quiz.current_question()
        total = len(quiz.questions)
        current = quiz.current_index + 1
        self.progress_var.set(f"Вопрос {current} из {total}")

        self.question_var.set(q["question"])
        for i, rb in enumerate(self.radio_buttons):
            if i < len(q["options"]):
                rb.config(text=f"{i + 1}. {q['options'][i]}", state="normal")
            else:
                rb.config(text="", state="disabled")

        self.choice.set(-1)  # сбрасываем выбор

    def submit(self):
        if self.choice.get() == -1:
            return  # ничего не выбрано

        quiz = self.controller.quiz
        quiz.submit_answer(self.choice.get())

        if quiz.is_finished():
            self.controller.show_frame("ResultFrame")
        else:
            self.load_question()