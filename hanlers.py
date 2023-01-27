# -*- coding: utf-8 -*-
"""

"""
__all__ = ["HandlersDB"]

from connect_db import HandlerRecord


class HandlersDB:
    def __init__(self):
        self.handle = HandlerRecord()

    def erase_all_users(self):
        self.handle.delete_all_records()

    def record_result(self, name: str, corr_answ: int, wrong_answ: int) -> None:
        self.handle.write_db(names=name, correct_answer=corr_answ, wrong_answer=wrong_answ)
