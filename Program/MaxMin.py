# MaxMin.py

import tkinter
import FunctionMain

class MaxMin(FunctionMain.Function):
    def __init__(self, parent):
        super(MaxMin, self).__init__(parent)

        # Widgets
        # ラベル, 入力ボックス, 決定ボタン, 表示ラベル 
        self.lblNum = tkinter.Label(self, text="右の枠に数字を入力してください", anchor=tkinter.W)

        # 10個の入力ボックスを生成
        self.numEntry = []
        for i in range(0, 10):
            self.numEntry.append(tkinter.Entry(self))

        self.btn = tkinter.Button(self, text="決定", command=self.executeGUI)
        self.txt = "結果表示:"
        self.lblResult = tkinter.Label(self, text=self.txt, anchor=tkinter.W)
        
        # Layout
        self.lblNum.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)
        for i in range(0, 10):
            self.numEntry[i].grid(row=i+1, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.btn.grid(row=11, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.lblResult.grid(row=12, column=0, padx=2, pady=2, sticky=tkinter.W)


    # 結果表示のラベル切り替えのための関数
    def executeGUI(self):

        # 10個の値を取得
        num = []
        for i in range(0, 10):
            entry = self.numEntry[i].get().strip()
            if entry !=  "":
                entry = int(entry)
                num.append(entry)

        # execute関数を実行
        num = self.execute(num)
        txt = str(num)

        # txt = "半角の数字を入力してください。"
        
        self.lblResult2 = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblResult2.grid(row=12, column=1, padx=2, pady=2, sticky=tkinter.W)



    # 最大値取得の関数
    def execute(self, list1):
        # 仮の最大値tmpMax
        tmpMax = list1[0]

        for i in range(1, 10):
            if tmpMax < list1[i]:
                tmpMax = list1[i]
        
        return tmpMax


