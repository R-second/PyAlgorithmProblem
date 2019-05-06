# MainWindow.pyw
import tkinter

class MainWindow(tkinter.Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)

        #Widgets
        self.btn1 = tkinter.Button(self, text="素数判定＋素因数分解", command=self.btn_Search)
        self.btn2 = tkinter.Button(self, text="フィボナッチ数列の出力", command=self.btn_Search)
        self.btn3 = tkinter.Button(self, text="最大公約数出力", command=self.btn_Search)
        self.btn4 = tkinter.Button(self, text="最大値/最小値判定", command=self.btn_Search)
        self.btn5 = tkinter.Button(self, text="ソート", command=self.btn_Search)
        self.btn6 = tkinter.Button(self, text="万年カレンダー", command=self.btn_Search)


