# main.py
import tkinter
import WindowGUI
import PrimeFactor

# funcクラスを定義
class func:
    primeFactor = PrimeFactor.PrimeFactor()
    # functionListにそれぞれの処理を順に代入
    functionList = [primeFactor, primeFactor, primeFactor, primeFactor, primeFactor, primeFactor]

# main処理の関数
def main():
    application = tkinter.Tk()
    application.title("mainWindow")
    window = WindowGUI.MainWindow(application)
    application.protocol("WM_DELETE_WINDOW", window.quit)
    application.mainloop()

if __name__ == '__main__':
    main()
