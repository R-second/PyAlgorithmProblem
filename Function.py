# Function.py

import tkinter

# 上位クラスFunctionクラス（関数はすべてこれを継承する）
class Function(tkinter.Frame):

    def __init__(self, parent):
        super(Function, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)
    
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
        
        # Widgets # 実行するプログラムを表示するラベルを用意
        txt = "プログラム 1. 素数判定+素因数分解 を実行します。"
        self.lblTitle = tkinter.Label(self, text=txt, anchor=tkinter.W, width=45)
        self.lblNum = tkinter.Label(self, text="   右の枠に数字を入力してください", anchor=tkinter.W, width=20)
        self.numEntry = tkinter.Entry(self, width=22)
        self.btn = tkinter.Button(self, text="決定", command=self.execute)
        
        self.lblTitle.grid(row=0, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.lblNum.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)
        self.numEntry.grid(row=1, column=1, padx=2, pady=2, sticky=tkinter.W)
        self.btn1.grid(row=1, column=2, padx=2, pady=2, sticky=tkinter.W)

    def execute(self):
        pass
