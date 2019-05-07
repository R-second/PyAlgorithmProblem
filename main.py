# main.py
import tkinter
import Window

class func:
    def func1():
        print(1)
    def func2():
        print(2)
    def func3():
        print(3)
    def func4():
        print(4)
    def func5():
        print(5)
    def func6():
        print(6)
    # functionList = [func1(), func2(), func3(), func4(), func5(), func6()]

# main処理の関数
def main():
    application = tkinter.Tk()
    application.title("mainWindow")
    window = Window.MainWindow(application)
    application.protocol("WM_DELETE_WINDOW", window.quit)
    application.mainloop()

if __name__ == '__main__':
    main()




# def main():
#     print("このプログラムでは以下のアルゴリズムを試すことができます。")
#     print("1. 素数判定＋素因数分解")
#     print("2. フィボナッチ数列の出力")
#     print("3. 最大公約数の出力")
#     print("4. 最大値・最小値の判定")
#     print("5. ソート")
#     print("6. 万年カレンダー")
#     st = input("試したいアルゴリズムの数字を半角で入力してください。（終了したい場合はq）＞")

#     while st == "q" or int(st)>7:
#         print("不適切な文字が入力されました。半角数字かqを入力してください。")
#         st = input("試したいアルゴリズムの数字を半角で入力してください。（終了したい場合はq）＞")
    
#     num = int(st)
#     while num<7:
#         if num==1:
#             print("1を実行します。")
#             break
#         elif num==2:
#             print("2を実行します。")
#             break
#         elif num==3:
#             print("3を実行します。")
#             break
#         elif num==4:
#             print("4を実行します。")
#             break
#         elif num==5:
#             print("5を実行します。")
#             break
#         elif num==6:
#             print("6を実行します。")
#             break

# main()