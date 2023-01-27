# -*- coding: utf-8 -*-
"""

"""

__all__ = ["SelectResult"]

from click import secho as sc

from connect_db import HandlerRecord


class SelectResult:
    def __init__(self):
        self.handler = HandlerRecord()
        self.count: int = 0
        self.corr_answ: int = 0
        self.wron_answ: int = 0

    def select_result(self, name):
        self.count, self.corr_answ, self.wron_answ = self.handler.select_by_name(name)
        sc(f"  Всего пройдено тестов: {self.count}", fg="cyan")
        sc(f"  Правильных ответов:    {self.corr_answ}", fg="green")
        sc(f"  Неправильных ответов:  {self.wron_answ}\n", fg="red")

    def select_users(self):
        users = self.handler.select_all_users()
        sc(f"  Имя пользователя  | количество тестов | правильных ответов | "
           f"неправильных ответов", fg="white")
        for i in users:
            self.count, self.corr_answ, self.wron_answ = self.handler.select_by_name(i)
            sc(f"{i: ^19} | {self.count: ^17} | {self.corr_answ: ^18} | "
               f"{self.wron_answ: ^17}", fg="white")
        sc(f"{'=' * 85}\n", fg="blue")
