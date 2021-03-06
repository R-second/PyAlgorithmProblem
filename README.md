# PyAlgorithmProblem
## このプログラムの概要
このプログラムは独断でセレクションした以下の６種類のアルゴリズム問題の入出力をGUIで確認できるようにしたものです。  
- 素数判定
- フィボナッチ数列
- 最大公約数出力
- 配列内の最大値判定
- ソート
- 万年カレンダー

プログラムは[programフォルダ](https://github.com/R-second/PyAlgorithmProblem/tree/master/Program)に全て入っています。
Main部分のプログラムの解説は[README-main.md](https://github.com/R-second/PyAlgorithmProblem/blob/master/README-main.md)に示し、各アルゴリズムの解説は[README-algorithm.md](https://github.com/R-second/PyAlgorithmProblem/blob/master/README-algorithm.md)に示しています。

プログラムを動かしたい時は、[programフォルダ](https://github.com/R-second/PyAlgorithmProblem/tree/master/Program)ごと、ダウンロードし、 `python main.py` を実行してください。

全てpythonで実装しており、多少のオブジェクト指向も取り入れています。  
1年生のアルゴリズム問題回答用 ＋ 自分のスキル確認用 ＋ gitHubコマンド練習用 として作成しました。  
もっとも基本的な（＝高度な知識を必要とせず、プログラム初心者にとって読みやすい）アルゴリズムで実装しています。もちろん、同じ問題でもこれ以外にもっと簡単な方法やもっと高速なやり方が存在します。あくまで一例として紹介しているだけです。


以下の点にまだまだ問題が見られます。
- アルゴリズム単独で動くようなクラスの規格化が明確でない。
- オブジェクト指向の使い分けが汚い。
- 入力の例外処理を行っていない。
- 文字列周りの処理が汚い。

全体的にもっと綺麗にできるので、今後、改善する予定です。