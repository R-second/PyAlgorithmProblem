# Sort.py

import tkinter
import FunctionMain

class Sort(FunctionMain.Function):
    def __init__(self, parent):
        super(Sort, self).__init__(parent)

        # Widgets
        # ラベル, 入力ボックス, 決定ボタン, 表示ラベル 
        self.lblNum = tkinter.Label(self, text="右の枠に数字を入力してください（10個全て入力する必要はありません。）", anchor=tkinter.W)

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
            num.append(int(self.numEntry[i].get()))
        
        # execute関数を実行
        txt = self.execute(num)

        # txt = "半角の数字を入力してください。"
        
        self.lblResult2 = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblResult2.grid(row=12, column=1, padx=2, pady=2, sticky=tkinter.W)



    # 昇順に並べ替えの関数
    def execute(self, list1):
        elem = len(list1)  # 要素数を取得

        # topに"最小値-1"を格納してループ
        for top in range(0, elem-1):
            # top以下で最小値を探し、topの位置に格納
            for i in range(elem-1, top-1, -1):
                if list1[i] < list1[i-1]:
                    tmp = list1[i]
                    list1[i] = list1[i-1]
                    list1[i-1] = tmp
        
        txt = ""
        for i in range(0, elem):
            txt = txt + str(list1[i]) + ", "
        
        return txt



