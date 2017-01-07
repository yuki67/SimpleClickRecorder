# -*- coding: utf-8 -*-
import time
import argparse
from clickRecorder import ClickRecorder


def make_parser():
    parser = argparse.ArgumentParser(description="Record clicks.")
    parser.add_argument("-n", dest="name", action="store", default="log_click",
                        help="Name of the log file. Default = \"log_click\"")
    return parser


def prompt():
    args = make_parser().parse_args()
    logger = ClickRecorder(args.name)
    print("Note : When recording starts, a transparent window will appear.")
    print("Note : Click on the transparent window to record clicks.")
    print("Note : Delete window to stop recording.")
    print("Note : 記録が始まると、透明なウィンドウが現れます。")
    print("Note : 透明なウィンドウをクリックすると記録されます。")
    print("Note : 記録をやめるには、透明なウィンドウを消してください。")
    print("--Press enter to start recording.--")
    print("--Enterで記録を開始します。--")
    input()
    print("--Recording starts in 3 seconds.--")
    print("--3秒後に記録を開始します。--")
    time.sleep(3.0)
    logger.startLog()
    print("end.")
    print("終了")
    print("Log was recorded in " + args.name + ".py")
    print("記録が以下のファイルに保存されました。" + args.name + ".py")

prompt()
