# [MaD] Notebook スタイルガイド

## Knitr 用のラベル付けルール


講義資料の開発には次のように進める。

- Jupyter Notebook で挿入用のコードを章ごとに作成する。
- nbconvert で Jupyter Notebook を Python スクリプトに変換する。
- knitr の [code externalization](https://yihui.org/knitr/demo/externalization/) でコードを挿入する。


### 基礎知識

Knitr は，外部ファイルのコードセクションにラベル付けを行うと，セクション単位のインポートができる。次のような形式を用いる。 `#----` に続くテキストがコードインポート時のキーになる。

    ## chXX.py
    
    #---- ref-label-1
    print('some code')
    
    #---- ref-label-2
    print('not shown')

LyX ファイルに以下の TeX Code を挿入すると，`print('come code')` とその結果が出力文書に挿入される。

    ## chXX.lyx / chXX.Rnw
    
    <<engine='R', echo=FALSE>>=
    knitr::read_chunk('code.py')
    @
    
    <<ref-label-1>>=
    @

なお，この講義ノートでは主に Python コードを紹介するので，グローバルに `engine='python'` と設定している。そのため，`engine='R'` を明示的に書いている。

### ローカルルール

前述の通り，章ごとに Python スクリプトが生成されている。対応関係は次の通り。

- Jupyter/ch01.ipynb → Lecture Note/Python/ch01.py → Lecture Note/ch01.lyx
- Jupyter/ch02.ipynb → Lecture Note/Python/ch02.py → Lecture Note/ch02.lyx
- etc.

各 chXX.py （つまるところ，生成元となる chXX.ipynb）には次の形式で**チャンクラベルの原型**を付与している。

    #---- chXX/description/option

例えば，次のようにする。`dnr` は "do not run" の略である。

    #---- ch02/numpy-example-code/dnr

最後の部分を使って，適切な Knitr のチャンクオプションが自動的にセットされるようにする。これは，Jupyter Notebook での開発時の意図と，挿入時のオプション設定に矛盾が生じないようにするための措置である。


| option | チャンクオプション | コード表示 | コード実行 | 結果表示 | その他 |
|----------------|----------------------------------|------------|------------|----------|-------------------------------|
| dnr | `eval=FALSE` | Default | Default | Default |  |
| noinc | `include=FALSE` | × | ○ | × |  |
| graphics | `include=FALSE, fig.show='hide'` | × | ○ | × | `\includegraphics` で図を表示 |
| plot     | `fig.show='hide'`  | ○ | ○ | × | `\includegraphics` で図を表示 |


チャンクのラベルの実体は「原型」の最後の部分（option）を外したものとなる。したがって，

- 相互参照にチャンクラベルを用いる場合は，`chXX/description` などを使う。
- 画像ファイルは `chXX/description-1.pdf` などとなる。結果的に画像ファイルは章ごとにフォルダ分けされる。


