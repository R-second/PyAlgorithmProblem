# Function.py

import tkinter

# 上位クラスFunctionクラス（関数はすべてこれを継承する）
class Function(tkinter.Frame):

    def __init__(self, parent):
        super(Function, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)

        # 実行するプログラムを表示するラベルを用意
        txt = "プログラム 1. 素数判定 を実行します。"
        self.lblTitle = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblTitle.grid(row=0, column=0, padx=2, pady=2, sticky=tkinter.W)
        
    
    def quit(self, event=None):
        self.parent.destroy()


class FunctionList:
    @classmethod
    def functionMain(self, num):
        application2 = tkinter.Tk()
        application2.title("subWindow")
        subWindow = PrimeFactor(application2) # SubWindowクラスをsubWindow変数に代入
        application2.protocol("WM_DELETE_WINDOW", subWindow.quit)
        application2.mainloop()

class PrimeFactor(Function):
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


    def executeGUI(self):
        entry = self.numEntry.get()
        num = int(entry)
        txt = self.execute(num)

        # txt = "半角の数字を入力してください。"
        
        self.lblResult2 = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblResult2.grid(row=2, column=1, padx=2, pady=2, sticky=tkinter.W)

    def execute(self, num):
        flag = 1
        for i in range(2, num):
            if num % i == 0:
                flag = 0
                break
        
        if flag==1:
            return "素数です。                    "
        else:
            return "素数ではありません  "


