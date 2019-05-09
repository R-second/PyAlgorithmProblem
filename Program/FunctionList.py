# FunctionList.py
import tkinter
import PrimeFactor
import Fibonacci
import Gcd
import MaxMin
import Sort
import Calendar

class FunctionList:
    # functionListにアルゴリズムの名称を設定
    functionList = ["素数判定", "フィボナッチ数列の出力", "最大公約数出力", "最大値判定", "ソート", "万年カレンダー"]

    @classmethod
    def functionMain(cls, num):
        # subWindowを作成
        application2 = tkinter.Tk()
        application2.title("subWindow")

        # 引数numに応じてインスタンスの生成を変更
        if num == 0:
            subWindow = PrimeFactor.PrimeFactor(application2)
        elif num == 1:
            subWindow = Fibonacci.Fibonacci(application2)
        elif num == 2:
            subWindow = Gcd.Gcd(application2)
        elif num == 3:
            subWindow = MaxMin.MaxMin(application2)
        elif num == 4:
            subWindow = Sort.Sort(application2)
        else:
            subWindow = Calendar.Calendar(application2)
        
        application2.protocol("WM_DELETE_WINDOW", subWindow.quit)
        application2.mainloop()




