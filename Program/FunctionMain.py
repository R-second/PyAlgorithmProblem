# Function.py

import tkinter


# 上位クラスFunctionクラス（関数はすべてこれを継承する）
class Function(tkinter.Frame):

    def __init__(self, parent):
        super(Function, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)

        # 実行するプログラムを表示するラベルを用意
        txt = "プログラムを実行します。"
        self.lblTitle = tkinter.Label(self, text=txt, anchor=tkinter.W)
        self.lblTitle.grid(row=0, column=0, padx=2, pady=2, sticky=tkinter.W)
        
    # windowを正常に閉じるための関数 quit
    def quit(self, event=None):
        self.parent.destroy()
    
    # GUIを定義するexecuteGUI（継承後にオーバーライド）
    def executeGUI(self):
        pass

    # メインの処理を実行するexecute（継承後にオーバーライド）
    def execute(self):
        pass
