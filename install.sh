#!/bin/bash

export LC_CTYPE=en_US.UTF-8
clear

cd Desktop
git clone https://github.com/codelao/Pocket-Casino.git
echo alias casino="python3 ~/Pocket-Casino/casino.py" >> 

$shell=echo $0

if [[ "$shell" == "-zsh" || "$shell" == *"-bash"* ]]; then

