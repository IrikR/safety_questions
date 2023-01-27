# -*- coding: utf-8 -*-
"""
Модуль в котором происходит обработка считанных данных из БД,
вывод информации в CLI,
прием данных от пользователя,
запись результатов в БД.
"""

__all__ = ["Question"]

from random import randrange

from connect_db import HandlerRecord
from utils import CLILog


class Question:
    def __init__(self):
        self.handler = HandlerRecord()
        self.msg = CLILog()

    @staticmethod
    def counter():
        """
        Функция счетчик, для подсчета правильных и неправильных ответов.
        """
        count = 0

        def inner(value: int) -> int:
            nonlocal count
            count += value
            return count

        return inner

    def io_question(self):
        """
        Функция ввода-вывода вопросов и ответов в CLI.
        Не принимает ни каких аргументов.
        И возвращает True при правильном ответе, и False при неправильном ответе.
        Берет рандомно по одному вопросу из каждой темы и выводит их на экран.
        :return:
        """
        corr_answer = self.counter()
        res_corr_ans: int = 0
        wrong_answer = self.counter()
        res_wrong_ans: int = 0
        for i in range(1, 8):
            number_of_questions, *_ = self.handler.number_of_questions(question_topic=f"team_{i}")
            question: int = randrange(1, number_of_questions)
            quest_full = self.handler.read_question(id_question=question, question_topic=f"team_{i}")
            correct_answer: int = int(quest_full[6])
            theme = quest_full[7]
            quest = quest_full[0]
            ques_1 = quest_full[1:6]
            self.msg.print_msg(f"\n{theme}\n", "skyblue")
            self.msg.print_msg(f"{quest}\n", "skyblue")
            for j in ques_1:
                self.msg.print_msg(j, "gray")
            answer = int(input("ответ:\t"))
            if answer == correct_answer:
                self.msg.print_msg("правильный ответ", "green")
                res_corr_ans = corr_answer(1)
            elif answer != correct_answer:
                self.msg.print_msg("неправильный ответ", "red")
                self.msg.print_msg(f"правильный ответ: {correct_answer}", "orange")
                res_wrong_ans = wrong_answer(1)
        self.msg.print_msg(f"\n\tПравильных ответов: {res_corr_ans}", "green")
        self.msg.print_msg(f"\tНеправильных ответов: {res_wrong_ans}\n", "red")
        self.msg.print_msg("", "gray")
        return res_corr_ans, res_wrong_ans

    def record_result(self, name, corr_answ, wrong_answ):
        self.handler.write_db(name, corr_answ, wrong_answ)


if __name__ == "__main__":
    ques = Question()
    corr_ans, wrong_ans = ques.io_question()
    print(corr_ans, wrong_ans)
