# PyAlgorithmProblem プログラムMain部分の解説
## 使用したモジュールの紹介
このプログラムではGUIの実装のためにtkinterを使用しました。
そのため、どの.pyファイルにおいても、 `import tkinter` を行っています。

## main.py
ここでは、 `main()` を定義し、実行しています。`main()` の動作は以下の通りです。
1. tkinterのウィンドウを定義し、表示するクラス `WindowGUI.MainWindow()` を呼び出す。
2. ウィンドウを閉じるバツ印が押された時に正常に終了できるように、 `window.quit` を使用
3. `mainloop()` を回す。

## WindowGui.py
ここでは、 `Window` クラスと、それを継承した `MainWindow` クラスを定義しています。 `MainWindow` クラスは、`main.py` から呼び出されるクラスです。

### Windowクラス
ウィンドウを表示するもっとも基本的な部分のみを備えたクラスです。他のクラスに継承され使われます。  
`__init__` で、ウィンドウの定義を行っています。  
`quit` は、ウィンドウを閉じるバツ印が押された時に正常に終了するための関数です。

### MainWindowクラス
#### __init__
`Window`クラスを継承したメインのウィンドウを起動するクラスです。  
btn1〜6までの変数に、tkinterのButtonを代入します。その際、表示するテキスト部分にはアルゴリズムの名称、クリックされた時の処理として`subWindow()`を定義します。`subWindow()`はボタン番号を引数として持たせています。  
その後、btn1~6までを上から順にレイアウトしています。

#### subWindow
FunctionListクラスのfunctionMain関数を実行する処理を行っています。その際、functionMain関数の実引数は自身の仮引数です。

## FunctionList.py
全てのアルゴリズム処理のため、全てのアルゴリズムクラスをimportしています。

### FunctionListクラス
アルゴリズムの名称をfunctionListのリストに格納しています。  
`functionMain()`では、subWindowを作成し、引数の値に応じて、インスタンスの生成を変更しています。引数に応じたインスタンスは先に解説した、MainWindowクラスのbtn番号と対応しています。

## FunctionMain.py
### Functionクラス
全てのアルゴリズムに継承させるための上位的なクラスとして`Function`クラスを定義しています。  
コンストラクタ（`__init__`）で、ウィンドウの生成とタイトルを表示するラベルの定義とレイアウトを実行。  
また、windowを正常に閉じるための`quit()`関数と、GUIを定義する`executeGUI()`、メインのアルゴリズム処理を実行する`execute()`関数を定義しています。`executeGUI`と`execute()`は、継承後にオーバーライドされるため、passとしています。