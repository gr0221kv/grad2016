#!/bin/sh
make clean
make FONTMAP=/usr/local/texlive/2014/texmf-dist/fonts/map/dvipdfmx/jfontmaps/hiragino-pron/ptex-hiragino-pron.map
mv -f thesis.pdf m-tsushima.pdf
