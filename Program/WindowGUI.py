# WindowGUI.py
import tkinter
from FunctionList import FunctionList

# 上位クラスWindow（MainWindowとSubWindowを継承させる）
class Window(tkinter.Frame):

    def __init__(self, parent):
        super(Window, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)
    
    # windowを正常に閉じるための関数 quit
    def quit(self, event=None):
        self.parent.destroy()


# Windowクラスを継承したMainWindowクラス
class MainWindow(Window):

    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)

        self.btn = []
        #Widgets
        #ボタンを６つ用意する（クリックされたら、subWindow関数の引数にボタン番号を渡して実行）
        self.btn1 = tkinter.Button(self, text="1. 素数判定", command=lambda:self.subWindow(0))
        self.btn2 = tkinter.Button(self, text="2. フィボナッチ数列の出力", command=lambda:self.subWindow(1))
        self.btn3 = tkinter.Button(self, text="3. 最大公約数出力", command=lambda:self.subWindow(2))
        self.btn4 = tkinter.Button(self, text="4. 最大値判定", command=lambda:self.subWindow(3))
        self.btn5 = tkinter.Button(self, text="5. ソート", command=lambda:self.subWindow(4))
        self.btn6 = tkinter.Button(self, text="6. 万年カレンダー", command=lambda:self.subWindow(5))

        #Layout
        self.btn1.grid(row=0, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.btn2.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.btn3.grid(row=2, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.btn4.grid(row=3, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.btn5.grid(row=4, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.btn6.grid(row=5, column=0, padx=2, pady=2, sticky=tkinter.W)

    # ボタンがクリックされた時の処理を実行するsubWindow関数
    def subWindow(self, num):
        FunctionList.functionMain(num)
