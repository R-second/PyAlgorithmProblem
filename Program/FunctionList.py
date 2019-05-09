# FunctionList.py
import tkinter
import PrimeFactor
import Fibonacci
import Gcd

class FunctionList:
    functionList = ["素数判定", "フィボナッチ数列の出力", "最大公約数出力", "最大値判定", "ソート", "万年カレンダー"]

    @classmethod
    def functionMain(cls, num):
        application2 = tkinter.Tk()
        application2.title("subWindow")

        if num == 0:
            subWindow = PrimeFactor.PrimeFactor(application2)
        elif num == 1:
            subWindow = Fibonacci.Fibonacci(application2)
        elif num == 2:
            subWindow = Gcd.Gcd(application2)
        else:
            subWindow = MaxMin.MaxMin(application2)
        
        application2.protocol("WM_DELETE_WINDOW", subWindow.quit)
        application2.mainloop()




