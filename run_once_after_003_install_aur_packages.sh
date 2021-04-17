#!/bin/bash

yay -Syu
yay -S --needed - < ~/.config/aur-pkglist.txt
