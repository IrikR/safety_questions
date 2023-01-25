# -*- coding: utf-8 -*-
"""

"""
from random import randrange

from connect_db import ReadDB
from utils import CLILog


class Question:
    def __init__(self):
        self.read_db = ReadDB()
        self.msg = CLILog()

    def io_question(self):
        for i in range(1, 8):
            number_of_questions, *_ = self.read_db.number_of_questions(question_topic=f"team_{i}")
            question: int = randrange(1, number_of_questions)
            ques = self.read_db.read_question(id_question=question, question_topic=f"team_{i}")
            correct_answer: int = int(ques[6])
            theme = ques[7]
            quest = ques[0]
            ques_1 = ques[1:6]
            self.msg.print_msg(f"\n{theme}\n", "skyblue")
            self.msg.print_msg(f"{quest}\n", "skyblue")
            for i in ques_1:
                self.msg.print_msg(i, "gray")
            answer = int(input("ответ:\t"))
            if answer == correct_answer:
                self.msg.print_msg("правильный ответ", "green")
            elif answer != correct_answer:
                self.msg.print_msg("неправильный ответ", "red")
                self.msg.print_msg(f"правильный ответ: {correct_answer}", "orange")


if __name__ == "__main__":
    ques = Question()
    ques.io_question()
