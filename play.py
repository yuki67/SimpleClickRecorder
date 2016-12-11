# -*- coding: utf-8 -*-
import datetime
import time
import argparse
from clickPlayer import ClickPlayer

parser = argparse.ArgumentParser(description="Play logged clicks.")
parser.add_argument(dest="logname", action="store", help="Name of log file.")
parser.add_argument("-d", dest="duration", action="store", required=False, type=float, default=10, help="Duration of time to play clicks (in seconds). Default = 10")
parser.add_argument("-r", dest="rate", action="store", required=False, type=float, default=0.5, help="Blank after each click (in seconds). Default = 0.5")
args = parser.parse_args()

player = ClickPlayer(args.logname)
print("Note : Play %s for %.1f seconds with %.3f seconds of blank after each clicks." % (args.logname, args.duration, args.rate))
print("Note : %sを%.1f秒間、クリックごとに%.3f秒の間をあけて再生します。" % (args.logname, args.duration, args.rate))
print("Note : To quit, drag mouse fast to upper left of the display.")
print("Note : 途中でやめるには、マウスをディスプレイの左上に持って行ってください。")
print("--press enter to start playing log.--")
print("--Enterで再生を開始します。--")
input()
print("--Playing starts in 3 seconds.--")
print("--3秒後に再生を開始します。--")
time.sleep(3.0)
player.play(args.duration, args.rate)
print("--End--")
print("--終了--")
