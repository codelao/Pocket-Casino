#!/bin/bash

export LC_CTYPE=en_US.UTF-8
clear

printf "Welcome to Pocket Casino installer!\n"

installation() {
if ! python3 --version; then
    clear
    printf "\033[31m! Script can't check Python3 version before continuing\033[0m\n"
    exit 1
else
	cd ~
    if ! git clone https://github.com/codelao/Pocket-Casino.git; then
        clear
        printf "\033[31m! Unable to clone repository\033[0m\n"
        exit 1
    else
        if ! ; then
            clear
            printf "\033[31m! Pip can't install SPT\033[0m\n"
            exit 1
        else
            rm -rf Screenshots-Parse-Tool
            printf "\033[32mPocket Casino was successfully installed.\033[0m\n"
            exit 0
        fi
    fi
fi
}


installation
