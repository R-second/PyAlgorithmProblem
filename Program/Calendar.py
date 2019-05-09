# Calendar.py

import tkinter
import FunctionMain

class Calendar(FunctionMain.Function):
    def __init__(self, parent):
        super(Calendar, self).__init__(parent)

        # Widgets
        # ラベル, 入力ボックス, 決定ボタン, 表示ラベル 
        self.lblYear = tkinter.Label(self, text="年を入力してください", anchor=tkinter.W)
        self.lblMonth = tkinter.Label(self, text="月を入力してください", anchor=tkinter.W)
        self.yearEntry1 = tkinter.Entry(self)
        self.monthEntry2 = tkinter.Entry(self)
        self.btn = tkinter.Button(self, text="決定", command=self.executeGUI)
        self.txt = "結果表示:"
        self.lblResult = tkinter.Label(self, text=self.txt, anchor=tkinter.W)
        
        # Layout
        self.lblYear.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.lblMonth.grid(row=2, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.yearEntry1.grid(row=1, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.monthEntry2.grid(row=2, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.btn.grid(row=3, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.lblResult.grid(row=4, column=0, padx=2, pady=2, sticky=tkinter.W)


    # 結果表示のラベル切り替えのための関数
    def executeGUI(self):
        
        # 入力を拾ってくる
        year = int(self.yearEntry1.get())

        month = int(self.monthEntry2.get())

        # execute関数を実行し、txtに代入
        cal = self.execute(year, month)
        
        # 結果表示ラベルを設定
        elem = len(cal)
        self.lblResult2 = []
        for i in range(0, elem):
            self.lblResult2.append(tkinter.Label(self, text=cal[i], anchor=tkinter.W))
            self.lblResult2[i].grid(row=4+i, column=1, padx=2, pady=2, sticky=tkinter.W)


    # 各月の日付を定義
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 最大公約数取得の関数
    def execute(self, y, m):

        # 閏年なら、２月を29日に変更
        if self.leapYear(y) == 1:
            self.month[2] = 29

        newDay = self.newYearDay(y)  # y年元日の曜日を取得
        day = self.firstDay(newDay, m) # newDay曜日の年のm月目の初日の曜日を取得
        txt = []
        txt.append("      SUN          MON        TUE       WED       THU       FRI       SAT")
        txt1 = "            "
        for i in range(0, day):
            txt1 = txt1 + "            "  # 前月を埋める最初のスペース
        
        for i in range(1, self.month[m]+1):
            if i < 10:
                txt1 = txt1 + str(i).rjust(4) + "         "
            else:
                txt1 = txt1 + str(i).rjust(4) + "        "
            day = day + 1
            if day == 7:
                txt.append(txt1)
                txt1 = "         "
                day = 0

        return txt


    # 閏年か判定
    def leapYear(self, y):
        flag = 0  #閏年と仮定
        if y % 4 == 0:
            flag = 1
        if y % 100 == 0:
            flag = 0
        if y % 400 == 0:
            flag = 1
        return flag


    # y年の元日の曜日を取得
    def newYearDay(self, y):
        d = 1
        for i in range(1, y):
            d = d + 1 + self.leapYear(i)
        d = d % 7
        return d

    # 元日の曜日がdのとき、m月1日の曜日を取得
    def firstDay(self, d, m):
        t = d
        for i in range(1, m):
            t = t + self.month[i]
        return t % 7