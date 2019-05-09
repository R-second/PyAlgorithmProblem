# main.py
import tkinter
import WindowGUI

# main処理の関数
def main():
    application = tkinter.Tk()
    application.title("mainWindow")
    window = WindowGUI.MainWindow(application)
    application.protocol("WM_DELETE_WINDOW", window.quit)
    application.mainloop()

if __name__ == '__main__':
    main()

