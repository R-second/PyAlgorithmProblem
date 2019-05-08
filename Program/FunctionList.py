# FunctionList.py
import tkinter
import PrimeFactor
import Fibonacci

class FunctionList:
    @classmethod
    def functionMain(self, num):
        application2 = tkinter.Tk()
        application2.title("subWindow")
        if num == 0:
            subWindow = PrimeFactor.PrimeFactor(application2)
        else:
            subWindow = Fibonacci.Fibonacci(application2)
        application2.protocol("WM_DELETE_WINDOW", subWindow.quit)
        application2.mainloop()




