# Fibonacci.py

import tkinter
import FunctionMain

class Fibonacci(FunctionMain.Function):
    def __init__(self, parent):
        super(Fibonacci, self).__init__(parent)

        self.btn = tkinter.Button(self, text="実行", command=self.executeGUI)

        self.btn.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)


    # 結果表示のラベル切り替えのための関数
    def executeGUI(self):

        txt = self.execute()
        
        self.lblResult2 = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblResult2.grid(row=2, column=0, padx=2, pady=2, sticky=tkinter.W)


    # フィボナッチ数列取得の関数
    def execute(self):
        # 最初の２項はあらかじめ定義
        a = 1
        b = 1
        txt = str(a) + ", " + str(b) + ","  # txtに文字列として代入

        while(a+b < 100):
            a = a + b   # 奇数項を定義

            # 100を超えたらbreak
            if a + b > 100:   
                txt = txt + str(a)
                break

            b = a + b # 偶数項を定義

            txt = txt + str(a) + ", " + str(b) + ", "  # txtに文字列として代入
        
        return txt

