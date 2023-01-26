# -*- coding: utf-8 -*-
"""

"""

__all__ = ["SelectResult"]

from connect_db import ReadDB
from utils import CLILog


class SelectResult:
    def __init__(self):
        self.conn_db = ReadDB()
        self.cli_log = CLILog()
        self.count: int = 0
        self.corr_answ: int = 0
        self.wron_answ: int = 0

    def select_result(self, name):
        self.count, self.corr_answ, self.wron_answ = self.conn_db.select_by_name(name)
        self.cli_log.print_msg(f"Всего пройдено тестов:\t{self.count}", "skyblue")
        self.cli_log.print_msg(f"Правильных ответов:\t{self.corr_answ}", "green")
        self.cli_log.print_msg(f"Неправильных ответов:\t{self.wron_answ}", "red")
