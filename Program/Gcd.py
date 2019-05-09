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
        
        # Layout
        self.lblNum.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.numEntry1.grid(row=1, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.numEntry2.grid(row=2, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.btn.grid(row=3, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.lblResult.grid(row=4, column=0, padx=2, pady=2, sticky=tkinter.W)


    # 結果表示のラベル切り替えのための関数
    def executeGUI(self):
        
        # 入力を拾ってくる（num1, num2に代入）
        entry1 = self.numEntry1.get()
        num1 = int(entry1)

        entry2 = self.numEntry2.get()
        num2 = int(entry2)

        # execute関数を実行し、txtに代入
        num = self.execute(num1, num2)
        txt = str(num)
        
        # 結果表示ラベルにtxtを表示
        self.lblResult2 = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblResult2.grid(row=4, column=1, padx=2, pady=2, sticky=tkinter.W)



    # 最大公約数取得の関数
    def execute(self, a, b):
        # 必ず a > b となるようにする
        if a < b :
            tmp = a
            a = b
            b = tmp

        # aをbで割った余りをremainderに代入
        remainder = a % b

        # 余りが0なら、割る数（b）を返す
        if remainder <= 0:
            return b
        
        # そうでなければ、割る数(b)と余りを変数とし、自身を再帰的に呼び出す
        return self.execute(b, remainder)