# PyAlgorithmProblem プログラムAlgorithm部分の解説
## common（共通する要素）
どのアルゴリズムクラスにおいても、以下のような関数と実行内容を持たせています。
- `__init__`：GUIに必要な要素の定義とレイアウト
- `executeGUI`：結果を表示するためのラベルを切り替えるための関数
- `execute`：アルゴリズムを実行するための関数

その他、必要であれば変数や関数を新たに定義しています。  
また、このREADME-algorithmにおいてはGUIの要素の定義やレイアウトについては控え、アルゴリズムの解説にとどめています。（主に`execute`の説明）

## PrimeFactor.py
与えられたint型の変数numが素数かどうかを判定するプログラム  
```flag = 1 ```
で、素数であると仮定して、
```python
for i in range(2, num):
    if num % i == 0:
        flag = 0
        break
```
２から、num-1（自分自身-1）までiを回し、numがiで割り切れた（＝素数ではない）時点で、`flag=0`とし、for文を抜ける処理を行う。

##  Fibonacci.py
[フィボナッチ数列](https://ja.wikipedia.org/wiki/フィボナッチ数#概要)を出力するプログラム

最初の２項（$F_{1}, F_{2}$）はあらかじめ定義しておく。
```python
a = 1
b = 1
```
また、フィボナッチ数が100以下の間、２項ずつ定義していく。
```python
while(a+b < 100):
    a = a + b   # 奇数項を定義
    # 100を超えたらbreak
    if a + b > 100:   
        break
    b = a + b # 偶数項を定義
```

##  Gcd.py
2つの数a, bが与えられた時に、その最大公約数を求めるプログラム  
ここでは、[ユークリッドの互除法](https://www.studyplus.jp/412)を用いた。

まず、aとbの大小関係を揃える。（必ず a>b）
```python
if a < b :
    tmp = a
    a = b
    b = tmp
```
aをbで割った余りが0なら、bで割った余りが最大公約数であり、そうでないなら、bと余りを元に同じ操作を繰り返す。
```python
# aをbで割った余りをremainderに代入
remainder = a % b

# 余りが0なら、割る数（b）を返す
if remainder <= 0:
    return b

# そうでなければ、割る数(b)と余りを変数とし、自身を再帰的に呼び出す
return self.execute(b, remainder)
```

## MaxMin.py
要素数10の配列list1が与えられた時に、そのうちの最大値を求めるプログラム

まず、要素の一番目を仮の最大値として定義
```tmpMax = list1[0]```
1から要素数の分だけiを回し、list1[i]が仮の最大値より大きければ、仮の最大値を書き換える。
```python
for i in range(1, 10):
    if tmpMax < list1[i]:
        tmpMax = list1[i]
```

## Sort.py
ある配列list1が与えられた時に、それらを小さい順（昇順）に並び替えるプログラム  
ここでは、バブルソートを使用しています。

