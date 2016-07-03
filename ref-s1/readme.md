# 修論

がんばる．

NGC.sty は色々と変えました．
コメント付いているのでカスタマイズが捗ると思います．

## 必要なもの

* TeX (dvipdfmx, pdflatex)
* GNU Make
* pdfcrop: PDFをトリミングするツール． apt, yum, brew なら pdf-tools とかに入っているかも．
* 各種TeXパッケージ: NGC.sty や thesis.tex の usepackage を見てください

TeXのパッケージは Fedora とか Ubuntu なら ``"texlive-*"`` で 30 分ほどお待ちください．
Mac TeX ならたぶんそのままで OK なはず．

## 注意

Make が適当なので，初回のビルドに失敗します．2, 3 回 Make してください．

## フォント

IPA フォントを埋め込む感じにしているので，インストールして下さい．

ヒラギノ (Mac付属) とか小塚 (Adobe付属) を持っている人は，
```
make FONTMAP=/usr/local/texlive/2014/texmf-dist/fonts/map/dvipdfmx/jfontmaps/hiragino-pron/otf-hiragino-pron.map
```
みたいにするとカッコ良いフォントが使えます．

http://oku.edu.mie-u.ac.jp/~okumura/texwiki/?Mac#i9febc9b

## 画像

画像は ``img/org/`` に PDF を入れて下さい．
``make`` で ``img/`` にトリミングした PDF を吐き出しますので，
``includegraphics`` では ``img/`` で指定して下さい．

``img/`` に ``*.pdf`` や ``*.xbb`` を入れると ``clean`` で消えるので注意．
