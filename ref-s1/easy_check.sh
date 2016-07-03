#!/bin/zsh
FILE=$1

for WORD in "異る" " つ" "收斂" "確立" "二つ" "おり，" "ゲートが "; do
    grep --color=auto -n $WORD $FILE
done
