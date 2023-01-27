# -*- coding: utf-8 -*-
"""
Модуль для взаимодействия основных программ с базой данных SQLite3.
Используется чтение и запись данных в БД.
"""

__all__ = ["HandlerRecord"]

import sqlite3
from datetime import datetime


class ConnectDB:
    """
    Родительский класс.
    Выполняет подключение к БД.
    """

    def __init__(self, way_reading):
        self.way_reading = way_reading

    def conn_db(self, inquiry):
        """
        Используется для чтения и записи данных
        :param inquiry: принимает строковый запрос SQL
        :return: возвращает прочитанные данные из БД
        """
        with sqlite3.connect('database/questions3.db3') as conn:
            cur = conn.cursor().execute(inquiry)
            match self.way_reading:
                case "fetchone":
                    return cur.fetchone()
                case "fetchall":
                    return cur.fetchall()
                case "put_record":
                    conn.commit()


class GetOneRecord(ConnectDB):
    """
    Метод для чтения по одной записи из БД
    """
    def __init__(self):
        super().__init__("fetchone")

    def get_one_record(self, inquiry):
        result = self.conn_db(inquiry)
        return result


class GetAllUsers(ConnectDB):
    """
    Метод для чтения всех пользователей из БД
    """
    def __init__(self):
        super().__init__("fetchall")

    def get_all_users(self, inquiry):
        result = self.conn_db(inquiry)
        return result


class PutOneRecord(ConnectDB):
    """
    Метод для записи в БД
    """
    def __init__(self):
        super().__init__("put_user")

    def put_result_user(self, inquiry):
        self.conn_db(inquiry)


class HandlerRecord:
    """
    Производит считывание данных из БД по заданным параметрам.
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
        self.get_one_record = GetOneRecord()
        self.get_all_users = GetAllUsers()
        self.put_record = PutOneRecord()

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
        inquiry = f"select questions, answer_1, answer_2, answer_3, answer_4, answer_5, correct_answer, " \
                  f"theme.theme from {them}, theme where id_questions={id_question} and " \
                  f"{them}.theme=theme.id_theme ;"
        return self.get_one_record.get_one_record(inquiry)

    def number_of_questions(self, question_topic: str):
        """
        Функция получает количество вопросов из таблицы заданной в параметре
        :param question_topic:
        :return:
        """

        them = self.themes_dict.get(f"{question_topic}")
        inquiry = f"select count (*) from {them}"
        return self.get_one_record.get_one_record(inquiry)

    def select_by_name(self, names: str):
        """
        SELECT COUNT(names) FROM "result" r WHERE names = '{names}';
        SELECT SUM(correct_answer) FROM "result" r WHERE names = '{names}';
        SELECT SUM(wrong_answer) FROM "result" r WHERE names = '{names}';
        SELECT COUNT(names), SUM(correct_answer), SUM(wrong_answer) FROM "result" r WHERE names = '{names}' ;
        """
        sample = f"SELECT COUNT(names), SUM(correct_answer), SUM(wrong_answer) " \
                 f"FROM \"result\" r WHERE names = '{names}' ;"
        return self.get_one_record.get_one_record(sample)

    def select_all_users(self):
        """
        SELECT DISTINCT names FROM "result" r ;
        """
        users_list: list = []
        select_users = f"SELECT DISTINCT names FROM \"result\" r ;"
        users = self.get_all_users.get_all_users(select_users)
        for i in users:
            users_list.append(i[0])
        return users_list

    def write_db(self, names: str, correct_answer: int, wrong_answer: int):
        """
        Функция используется для записи в БД результатов тестирования.
        """
        inquiry = f"INSERT INTO result (names, correct_answer, wrong_answer, date) " \
                  f"VALUES (\"{names}\", {correct_answer}, {wrong_answer}, \"{datetime.now()}\");"
        self.put_record.put_result_user(inquiry)


if __name__ == "__main__":
    # inquiry = f"select questions, answer_1, answer_2, answer_3, answer_4, answer_5, correct_answer, " \
    #              f"theme.theme from question_theme_1, theme where id_questions=1 and " \
    #              f"question_theme_1.theme=theme.id_theme ;"
    handler = HandlerRecord()
    print(handler.read_question(id_question=1, question_topic="team_1"))
    ques = handler.read_question(id_question=4,  question_topic="team_1")
    print(ques)
    # # ques = conn_db.read_db()
    corr_answer = ques[6]
    print(corr_answer)
    theme = ques[6]
    print(theme)
    ques_1 = ques[1:7]
    for j in ques_1:
        print(j)

    num, *_ = handler.number_of_questions(question_topic="team_1")
    print(num)
    handler.write_db(names="Вася Пупкин", correct_answer=4, wrong_answer=3)
    # print(datetime.time(datetime.now()))
    # print(datetime.now())
    count, corr_ans, wron_ans = handler.select_by_name("Вася Пупкин")
    print(count, corr_ans, wron_ans)
    print(handler.select_all_users())
