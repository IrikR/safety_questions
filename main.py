# -*- coding: utf-8 -*-
"""
Главный модуль.
Состоящий из класса Main, и функции main.
Запускает бесконечный цикл вывода в CLI меню программы:
    1 - для запуска тестов, последовательно выводит по одному тесту из каждой темы;
    2 - для смены пользователя;
    q - для выхода из программы.
 Так же по окончании теста производится запись результата в таблицу.
"""
import sys

from connect_db import WriteDB
from question import Question
from select_result import SelectResult
from utils import CLILog


class Main:

    def __init__(self):
        self.cli_log = CLILog()
        self.quest = Question()
        self.name: str = input("Введите ваше имя в формате Имя Фамилия\n")
        self.result_wr = WriteDB(self.name)
        self.select_name = SelectResult()
        self.res_correct_answer: int = 0
        self.res_wrong_answer: int = 0

    def main(self):
        """
        Главная функция для взаимодействия с пользователем.
        """
        while True:
            self.cli_log.print_msg(f"\t1 - пройти тест\n"
                                   f"\t2 - сметь пользователя\n"
                                   f"\t3 - просмотр результатов пользователя\n"
                                   f"\tq - выйти из программы", "gray")

            value = input("Выбор:\t")
            match value:
                case "1":
                    self.res_correct_answer, self.res_wrong_answer = self.quest.io_question()
                case "2":
                    self.relogin()
                case "3":
                    self.select_name.select_result(self.name)
                case "q":
                    sys.exit(0)
            self.result_wr.write_db(correct_answer=self.res_correct_answer, wrong_answer=self.res_wrong_answer)

    def relogin(self):
        """
        Функция для смены пользователя.
        """
        self.name = input("Введите ваше имя в формате Имя Фамилия\n")


if __name__ == "__main__":
    try:
        main = Main()
        main.main()
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    finally:
        sys.exit(0)
