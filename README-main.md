# PyAlgorithmProblem プログラムMain部分の解説
## 使用したモジュールの紹介
このプログラムではGUIの実装のためにtkinterを使用しました。
そのため、どの.pyファイルにおいても、 `import tkinter` を行っています。

## main.py
ここでは、 `main()` を定義し、実行しています。  
`main()` の動作は以下の通りです。
1. tkinterのウィンドウを定義し、表示するクラス `WindowGUI.MainWindow()` を呼び出す。
2. ウィンドウを閉じるバツ印が押された時に正常に終了できるように、 `window.quit` を使用
3. `mainloop()` を回す。

## WindowGui.py


