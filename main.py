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

from click import secho as sc

from question import Question
from select_result import SelectResult


class Main:

    def __init__(self):
        self.quest = Question()
        self.name: str = input("  Введите ваше имя в формате: Имя Фамилия\t")
        self.select_name = SelectResult()
        self.res_correct_answer: int = 0
        self.res_wrong_answer: int = 0

    def main(self):
        """
        Главная функция для взаимодействия с пользователем.
        """
        while True:
            sc(f"\t1 - пройти тест\n"
               f"\t2 - сметь пользователя\n"
               f"\t3 - просмотр результатов пользователя\n"
               f"\t4 - показать список пользователей\n"
               f"\tq - выйти из программы\n", fg="white")

            value = input("  Выбор:  ")
            match value:
                case "1":
                    self.res_correct_answer, self.res_wrong_answer = self.quest.io_question()
                    self.quest.record_result(name=self.name,
                                             corr_answ=self.res_correct_answer,
                                             wrong_answ=self.res_wrong_answer)
                case "2":
                    self.relogin()
                case "3":
                    self.select_name.select_result(self.name)
                case "4":
                    self.select_name.select_users()
                case "q":
                    sys.exit(0)

    def relogin(self):
        """
        Функция для смены пользователя.
        """
        self.name = input("  Введите ваше имя в формате: Имя Фамилия\t")


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
