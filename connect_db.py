#-*- coding: utf-8 -*-
"""
Модуль для взаимодействия основных программ с базой данных SQLite3.
Используется чтение и запись данных в БД.
"""

__all__ = ["ReadDB", "WriteDB"]

import sqlite3
from datetime import datetime


class ConnectDB:
    """
    Родительский класс.
    Выполняет подключение к БД.
    """
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
        """
        Используется для чтения данных из БД.
        """
        with sqlite3.connect('database/questions.db3') as conn:
            cur = conn.cursor()
            res = cur.execute(inquiry_id)
            one_result = res.fetchone()
            return one_result

    @staticmethod
    def read_all_users(inquiry_id):
        """
        Используется для чтения данных из БД.
        """
        with sqlite3.connect('database/questions.db3') as conn:
            cur = conn.cursor()
            res = cur.execute(inquiry_id)
            users: list = res.fetchall()
            return users

    @staticmethod
    def conn_db_write(inquiry_id):
        """
        Используется для записи данных в БД.
        """
        with sqlite3.connect('database/questions.db3') as conn:
            cur = conn.cursor()
            cur.execute(inquiry_id)
            conn.commit()


class ReadDB(ConnectDB):
    """
    Дочерний класс.
    Производит считывание данных из БД по заданным параметрам.
    """
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

    def select_by_name(self, names: str):
        """
        SELECT COUNT(names) FROM "result" r WHERE names = '{names}';
        SELECT SUM(correct_answer) FROM "result" r WHERE names = '{names}';
        SELECT SUM(wrong_answer) FROM "result" r WHERE names = '{names}';
        SELECT COUNT(names), SUM(correct_answer), SUM(wrong_answer) FROM "result" r WHERE names = '{names}' ;
        """
        sample = f"SELECT COUNT(names), SUM(correct_answer), SUM(wrong_answer) " \
                 f"FROM \"result\" r WHERE names = '{names}' ;"
        return self.conn_db(sample)

    def select_all_users(self):
        """
        SELECT DISTINCT names FROM "result" r ;
        """
        users_list: list = []
        select_users = f"SELECT DISTINCT names FROM \"result\" r ;"
        users = self.read_all_users(select_users)
        for i in users:
            users_list.append(i[0])
        return users_list


class WriteDB(ConnectDB):
    """
    Дочерний класс.
    Производит запись данных в БД по заданным параметрам.
    """
    def __init__(self):
        super().__init__()

    def write_db(self, names: str, correct_answer: int, wrong_answer: int):
        """
        Функция используется для записи в БД результатов тестирования.
        """
        inquiry = f"INSERT INTO result (names, correct_answer, wrong_answer, date) " \
                  f"VALUES (\"{names}\", {correct_answer}, {wrong_answer}, \"{datetime.now()}\");"
        self.conn_db(inquiry)


if __name__ == "__main__":
    read_db = ReadDB()
    # ques = read_db.read_question(id_question=4,  question_topic="team_1")
    # print(ques)
    # # ques = conn_db.read_db()
    # correct_answer = ques[6]
    # print(correct_answer)
    # theme = ques[6]
    # print(theme)
    # ques_1 = ques[1:7]
    # for i in ques_1:
    #     print(i)
    #
    # num, *_ = read_db.number_of_questions(question_topic="team_1")
    # print(num)
    # wr_db = WriteDB()
    # wr_db.write_db(names="Вася Пупкин", correct_answer=4, wrong_answer=3)
    # # print(datetime.time(datetime.now()))
    # # print(datetime.now())
    # count, corr_ans, wron_ans = read_db.select_by_name("Вася Пупкин")
    # print(count, corr_ans, wron_ans)
    print(read_db.select_all_users())
