# PrimeFactor.py
# 入力が素数かどうかを判定し、素因数分解の結果を返すプログラム

import tkinter
import FunctionMain

class PrimeFactor(FunctionMain.Function):
    def __init__(self, parent):
        super(PrimeFactor, self).__init__(parent)

        # Widgets
        # ラベル, 入力ボックス, 決定ボタン, 表示ラベル 
        self.lblNum = tkinter.Label(self, text="右の枠に数字を入力してください", anchor=tkinter.W)
        self.numEntry = tkinter.Entry(self)
        self.btn = tkinter.Button(self, text="決定", command=self.executeGUI)
        self.txt = "結果表示:"
        self.lblResult = tkinter.Label(self, text=self.txt, anchor=tkinter.W)
        
        self.lblNum.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.numEntry.grid(row=1, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.btn.grid(row=1, column=2, padx=2, pady=2, sticky=tkinter.W)
        self.lblResult.grid(row=2, column=0, padx=2, pady=2, sticky=tkinter.W)

    # 結果表示のラベル切り替えのための関数
    def executeGUI(self):
        entry = self.numEntry.get()
        num = int(entry)
        txt = self.execute(num)

        # txt = "半角の数字を入力してください。"
        
        self.lblResult2 = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblResult2.grid(row=2, column=1, padx=2, pady=2, sticky=tkinter.W)

    # 素数判定の関数（引数に判定したい数字）
    def execute(self, num):
        flag = 1  # 素数だと仮定
        for i in range(2, num):
            if num % i == 0:
                # 1つでも割り切れたらbreak
                flag = 0
                break
        
        if flag==1:
            return "素数です。                    "
        else:
            return "素数ではありません  "