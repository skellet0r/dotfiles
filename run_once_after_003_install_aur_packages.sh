#!/bin/bash

yay -Syu --noconfirm
yay -S --needed --noconfirm - < ~/.config/aur-pkglist.txt
