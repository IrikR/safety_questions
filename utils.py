# -*- coding: utf-8 -*-

__all__ = ["CLILog"]

import ctypes


class CLILog:
    """
        Вывод сообщений в консоль, с цветовой дифференциацией штанов
        Цвет        Текст   Фон
        Чёрный      30      40
        Красный     31      41
        Зелёный     32      42
        Жёлтый      33      43
        Синий       34      44
        Фиолетовый  35      45
        Бирюзовый   36      46
        Белый       37      47
    """

    def __init__(self):
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

    @staticmethod
    def print_msg(msg: str, msg_color: str):
        match msg_color:
            # case "black":
            #     print(f"\033[30m {msg}")
            case "red":
                print(f"\033[31m {msg}")
            case "green":
                print(f"\033[32m {msg}")
            case "orange":
                print(f"\033[33m {msg}")
            case "blue":
                print(f"\033[34m {msg}")
            case "purple":
                print(f"\033[35m {msg}")
            case "skyblue":
                print(f"\033[36m {msg}")
            case "gray":
                print(f"\033[37m {msg}")
            case _:
                print(f"\033[0;0m {msg}")

    @staticmethod
    def progress_bar(percent: int = 0, max_it: int = 100) -> None:
        """
        Функция предназначена для отображения в терминале прогресса выполнения.
        :param percent: Текущая итерация
        :param max_it: Максимум итераций
        """
        width = 60
        percent_tek = 100 / max_it * percent
        left = width * percent // max_it
        right = width - left
        print('\r[', '#' * left, ' ' * right, ']',
              f' {percent_tek:.0f}%',
              sep='', end='', flush=True)


if __name__ == "__main__":
    cli = CLILog()
    cli.print_msg(f"{'asdf' * 20}", "black")
    cli.print_msg(f"{'asdf' * 20}", "red")
    cli.print_msg(f"{'asdf' * 20}", "green")
    cli.print_msg(f"{'asdf' * 20}", "orange")
    cli.print_msg(f"{'asdf' * 20}", "blue")
    cli.print_msg(f"{'asdf' * 20}", "purple")
    cli.print_msg(f"{'asdf' * 20}", "skyblue")
    cli.print_msg(f"{'asdf' * 20}", "gray")
    cli.print_msg(f"{'asdf' * 20}", "black")
