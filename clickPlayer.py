# -*- coding: utf-8 -*-
import os
import datetime
import time
import sys

# pyautoguiかctypesをインポートしてclick()を作る
try:
    import pyautogui
    pyautogui_ok = True
    pyautogui.PAUSE = 0.0

    def click(button, x, y, rate):
        if button == 1:
            button = "right"
        else:
            button = "left"
        pyautogui.click(x, y, button=button)
        time.sleep(rate)
except ImportError:
    # pyautoguiが無くてもwindowsならどうにかなる
    if sys.platform == 'win32':
        import ctypes

        def click(button, x, y, rate):
            if button == 1:
                on = 2
                off = 4
            else:
                on = 8
                off = 16
            ctypes.windll.user32.SetCursorPos(x, y)
            ctypes.windll.user32.mouse_event(on, 0, 0, 0, 0)
            time.sleep(rate)
            ctypes.windll.user32.mouse_event(off, 0, 0, 0, 0)

    else:
        raise ImportError(
            "Please install pyautogui (sudo python -m pip install pyautogui).")


class ClickPlayer:

    def __init__(self, logName):
        # importするときに拡張子は不要
        self.record = __import__(os.path.basename(logName)[:-3]).record

    def play(self, duration, rate):
        endTime = datetime.datetime.now() + datetime.timedelta(seconds=duration)
        print("\a")
        while datetime.datetime.now() < endTime:
            for record in self.record:
                if datetime.datetime.now() < endTime:
                    click(record[0], record[1], record[2], rate)
                else:
                    break
