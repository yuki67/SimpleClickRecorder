# -*- coding: utf-8 -*-
import os
import tkinter


class ClickRecorder(object):

    def __init__(self, filename="log", rate=None):
        self.filename = os.path.abspath('.\\' + filename + '.py')
        self.rate = rate
        self.file = None
        self.root = None
        self.frame = None

    def startLog(self):
        self.setUpRoot()
        with open(self.filename, mode='w') as self.file:
            self.startFile()
            self.root.mainloop()  # ウィンドウが消えるとmainloopから抜ける
            self.endFile()

    def setUpRoot(self):
        self.root = tkinter.Tk()
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.title("Click Logger")
        self.root.attributes("-alpha", 0.5)
        self.root.attributes("-topmost", "true")
        self.root.geometry("%dx%d+%d+%d" % (width, height, 0, 0))
        self.frame = tkinter.Frame(self.root, width=width, height=height)
        # コールバック関数に複数の引数を渡す小技
        self.frame.bind("<Button-1>", lambda event: self.onLeftClick(event))
        self.frame.bind("<Button-3>", lambda event: self.onRightClick(event))
        self.frame.pack()

    def onLeftClick(self, event):
        self.addPointToFile(1, event.x, event.y)

    def onRightClick(self, event):
        self.addPointToFile(3, event.x, event.y)

    def startFile(self):
        # pythonソースコードの先頭部分を書く
        self.file.write('record = [')

    def addPointToFile(self, num, x, y):
        # pythonソースコードに[num, x, y]を追加する
        dx = self.root.winfo_rootx()  # ウィンドウのずれを補正
        dy = self.root.winfo_rooty()
        print("Logging : %d, %d, %d" % (num, x + dx, y + dy))
        # pythonでは[a,b]を[a, b,]と書いても問題ない
        self.file.write("[%d, %d, %d], " % (num, x + dx, y + dy))

    def endFile(self):
        # pythonソースコードの末尾部分を書く
        self.file.write(']\n')

    def addPointsToFile(self, data):
        # 使ってない
        self.file.write(str(data)[1:-1] + ',')
