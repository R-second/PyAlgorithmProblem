# Gcd.py

import tkinter
import FunctionMain

class Gcd(FunctionMain.Function):
    def __init__(self, parent):
        super(Gcd, self).__init__(parent)

        # Widgets
        # ラベル, 入力ボックス, 決定ボタン, 表示ラベル 
        self.lblNum = tkinter.Label(self, text="右の枠に数字を入力してください", anchor=tkinter.W)
        self.numEntry1 = tkinter.Entry(self)
        self.numEntry2 = tkinter.Entry(self)
        self.btn = tkinter.Button(self, text="決定", command=self.executeGUI)
        self.txt = "結果表示:"
        self.lblResult = tkinter.Label(self, text=self.txt, anchor=tkinter.W)
        
        self.lblNum.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.numEntry1.grid(row=1, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.numEntry2.grid(row=2, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.btn.grid(row=3, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.lblResult.grid(row=4, column=0, padx=2, pady=2, sticky=tkinter.W)


    # 結果表示のラベル切り替えのための関数
    def executeGUI(self):

        entry1 = self.numEntry1.get()
        num1 = int(entry1)

        entry2 = self.numEntry2.get()
        num2 = int(entry2)

        num = self.execute(num1, num2)
        txt = str(num)

        # txt = "半角の数字を入力してください。"
        
        self.lblResult2 = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblResult2.grid(row=4, column=1, padx=2, pady=2, sticky=tkinter.W)



    # フィボナッチ数列取得の関数
    def execute(self, a, b):
        if a < b :
            tmp = a
            a = b
            b = tmp

        remainder = a % b
        remainder = int(remainder)

        if remainder <= 0:
            return b
        
        return self.execute(b, remainder)