# Gcd.py

import tkinter
import FunctionMain

class MaxMin(FunctionMain.Function):
    def __init__(self, parent):
        super(MaxMin, self).__init__(parent)

        # Widgets
        # ラベル, 入力ボックス, 決定ボタン, 表示ラベル 
        self.lblNum = tkinter.Label(self, text="右の枠に数字を入力してください", anchor=tkinter.W)

        self.numEntry = []
        for i in range(0, 10):
            self.numEntry[i] = tkinter.Entry(self)
        # self.numEntry1 = tkinter.Entry(self)
        # self.numEntry2 = tkinter.Entry(self)
        # self.numEntry3 = tkinter.Entry(self)
        # self.numEntry4 = tkinter.Entry(self)
        # self.numEntry5 = tkinter.Entry(self)
        # self.numEntry6 = tkinter.Entry(self)
        # self.numEntry7 = tkinter.Entry(self)
        # self.numEntry8 = tkinter.Entry(self)
        # self.numEntry9 = tkinter.Entry(self)
        # self.numEntry10 = tkinter.Entry(self)

        self.btn = tkinter.Button(self, text="決定", command=self.executeGUI)
        self.txt = "結果表示:"
        self.lblResult = tkinter.Label(self, text=self.txt, anchor=tkinter.W)
        
        self.lblNum.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)

        for i in range(0, 10):
            self.numEntry[i].grid(row=i+1, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry1.grid(row=1, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry2.grid(row=2, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry3.grid(row=3, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry4.grid(row=4, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry5.grid(row=5, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry6.grid(row=6, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry7.grid(row=7, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry8.grid(row=8, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry9.grid(row=9, column=1, padx=2, pady=2, sticky=tkinter.W)
        # self.numEntry10.grid(row=10, column=1, padx=2, pady=2, sticky=tkinter.W)

        self.btn.grid(row=3, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.lblResult.grid(row=4, column=0, padx=2, pady=2, sticky=tkinter.W)


    # 結果表示のラベル切り替えのための関数
    def executeGUI(self):

        num = []

        for i in range(0, 10):
            num.append(self.numEntry[i].get())
        
        num = self.execute(num)
        txt = str(num)

        # txt = "半角の数字を入力してください。"
        
        self.lblResult2 = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblResult2.grid(row=4, column=1, padx=2, pady=2, sticky=tkinter.W)



    # フィボナッチ数列取得の関数
    def execute(self, list1):
        tmpMax = list1[0]
        for i in range(1, 10):
            if tmpMax > list1[i]:
                tmp = list1[i]
        
        return tmp


