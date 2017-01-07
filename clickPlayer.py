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

    def click(x, y, rate):
        pyautogui.click(x, y)
        time.sleep(rate)
except ImportError:
    # pyautoguiが無くてもwindowsならどうにかなる
    if sys.platform == 'win32':
        import ctypes

        def click(x, y, rate):
            ctypes.windll.user32.SetCursorPos(x, y)
            ctypes.windll.user32.mouse_event(0x02, 0, 0, 0, 0)
            time.sleep(rate)
            ctypes.windll.user32.mouse_event(0x04, 0, 0, 0, 0)
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
            for pos in self.record:
                if datetime.datetime.now() > endTime:
                    break
                else:
                    click(pos[0], pos[1], rate)
