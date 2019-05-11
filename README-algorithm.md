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
ここでは、[バブルソート](http://www.ics.kagoshima-u.ac.jp/~fuchida/edu/algorithm/sort-algorithm/bubble-sort.html)を使用しています。

以下の２重for文では下のような処理を行っています。
```python
# topに"最小値-1"を格納してループ
for top in range(0, elem-1):
    # top以下で最小値を探し、topの位置に格納
    for i in range(elem-1, top-1, -1):
        if list1[i] < list1[i-1]:
            tmp = list1[i]
            list1[i] = list1[i-1]
            list1[i-1] = tmp
```
1. 最小値を格納したい変数topを 0から`要素数-1`まで回す。
2. `要素数-1`から`top-1`まで-1ずつ回す。
3. もし、`list1[i]`がその一つ上の要素より小さければ、交換

## Calendar.py
ある年と月が与えられた時にその月のカレンダーを表示するプログラム

### 使用する変数とメソッド
- `month`：各月の日数を定義
- `execute()`：表示するプログラムのメインメソッド
- `leapYear(y)`：y年が閏年か判定するメソッド
- `newYearDay(y)`：y年の元日の曜日を取得するプログラム
- `firstDay(d, m)`：元日の曜日がdのとき、m月1日の曜日を取得するプログラム

また、ここで曜日は`[0, 1, 2, 3, 4, 5, 6] = ["日", "月", "火", "水", "木", "金", "土"]`と対応させています。

### executeメソッド
1. 閏年なら２月を29日に変更。
```python
if self.leapYear(y) == 1:
    self.month[2] = 29
```
2. y年m月1日の曜日を取得
```python
newDay = self.newYearDay(y)  # y年元日の曜日を取得
    day = self.firstDay(newDay, m) # newDay曜日の年のm月目の初日の曜日を取得
```
3. 前の月の空白を埋め、日付を取得

### leapYearメソッド
1. 閏年でないと仮定
``` flag = 0 ```
2. ４の倍数なら閏年。100の倍数なら閏年でない。400の倍数なら閏年。
```python
flag = 0  #閏年と仮定
    if y % 4 == 0:
        flag = 1
    if y % 100 == 0:
        flag = 0
    if y % 400 == 0:
        flag = 1
```

### newYearDayメソッド
1. 0年1月1日は1日
``` d = 1 ```
2. 1年からy年まで1ずつ足し（＝１年後の同日は曜日でいうと１つずれる）、閏年ならもう１足す（＝閏年ならもう１つずれる）
```python
for i in range(1, y):
    d = d + 1 + self.leapYear(i)
```
3. 7で割った余りを返す。
```python
d = d % 7
return d
```

### firstDayメソッド
1. 元旦の曜日は仮引数d
``` t = d ```
2. 1からm月まで月の日数を足し、７で割った余りを返す。
```python
for i in range(1, m):
    t = t + self.month[i]
return t % 7
```