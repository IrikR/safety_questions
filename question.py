# -*- coding: utf-8 -*-
"""
Модуль в котором происходит обработка считанных данных из БД,
вывод информации в CLI,
прием данных от пользователя,
запись результатов в БД.
"""

__all__ = ["Question"]

from random import randrange

from click import secho as sc

from connect_db import HandlerRecord


class Question:
    def __init__(self):
        self.handler = HandlerRecord()

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

    def io_question(self) -> [int, int]:
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
            sc(f"\n  {theme}\n", fg="cyan")
            sc(f"  {quest}\n", fg="cyan")
            for j in ques_1:
                sc(f"  {j}", fg="white")
            answer = int(input("  ответ:  "))
            if answer == correct_answer:
                sc(f"\tправильный ответ", fg="green")
                res_corr_ans = corr_answer(1)
            elif answer != correct_answer:
                sc(f"\tнеправильный ответ", fg="red")
                sc(f"\tправильный ответ: {correct_answer}\n", fg="yellow")
                res_wrong_ans = wrong_answer(1)
        sc(f"\tПравильных ответов: {res_corr_ans}", fg="green")
        sc(f"\tНеправильных ответов: {res_wrong_ans}\n", fg="red")
        return res_corr_ans, res_wrong_ans

    def record_result(self, name: str, corr_answ: int, wrong_answ: int) -> None:
        self.handler.write_db(names=name, correct_answer=corr_answ, wrong_answer=wrong_answ)


if __name__ == "__main__":
    ques = Question()
    corr_ans, wrong_ans = ques.io_question()
    print(corr_ans, wrong_ans)
