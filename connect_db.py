#-*- coding: utf-8 -*-
"""

"""

__all__ = ["ReadDB"]

import sqlite3


class ConnectDB:

    def __init__(self):
        self.themes_dict = {
            "team_1": "question_theme_1",
            "team_2": "question_theme_2",
            "team_3": "question_theme_3",
            "team_4": "question_theme_4",
            "team_5": "question_theme_5",
            "team_6": "question_theme_6",
            "team_7": "question_theme_7",
        }

    @staticmethod
    def conn_db(inquiry_id):
        with sqlite3.connect('database/questions.db3') as conn:
            cur = conn.cursor()
            res = cur.execute(inquiry_id)
            one_result = res.fetchone()
            return one_result


class ReadDB(ConnectDB):

    def __init__(self):
        super().__init__()

    def read_question(self, *, id_question: int, question_topic: str):
        """
        прочитать все: select * from question q ;
        прочитать строку по id=2: select * from question WHERE id_questions=2 ;
        select questions, answer_1, answer_2, answer_3, answer_4, answer_5, correct_answer, them.them
            from question_theme_3, them where id_questions=1 and question_theme_3.them=them.id_theme ;
        :type question_topic: str
        :param id_question:
        :param question_topic:
        :return:
        """

        them = self.themes_dict.get(f"{question_topic}")
        inquiry_id = f"select questions, answer_1, answer_2, answer_3, answer_4, answer_5, correct_answer, " \
                     f"theme.theme from {them}, theme where id_questions={id_question} and " \
                     f"{them}.theme=theme.id_theme ;"
        return self.conn_db(inquiry_id)

    def number_of_questions(self, question_topic: str):
        """
        Функция получает количество вопросов из таблицы заданной в параметре
        :param question_topic:
        :return:
        """

        them = self.themes_dict.get(f"{question_topic}")
        inquiry_id = f"select count (*) from {them}"
        return self.conn_db(inquiry_id)


if __name__ == "__main__":
    read_db = ReadDB()
    ques = read_db.read_question(id_question=4,  question_topic="team_1")
    print(ques)
    # ques = conn_db.read_db()
    correct_answer = ques[6]
    print(correct_answer)
    theme = ques[6]
    print(theme)
    ques_1 = ques[1:7]
    for i in ques_1:
        print(i)

    num, *_ = read_db.number_of_questions(question_topic="team_1")
    print(num)
