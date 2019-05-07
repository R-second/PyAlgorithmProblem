# PrimeFactor.py
# 入力が素数かどうかを判定し、素因数分解の結果を返すプログラム

import tkinter
from WindowGUI import Function

class PrimeFactor(Function):
    def gui(self):
        self.txtPrice = tkinter.Entry(self, width=22)
        self.txtPrice.grid(row=1, column=0, padx=2, pady=2, sticky=tkinter.W)
    
    def main(self):
        print("1")

