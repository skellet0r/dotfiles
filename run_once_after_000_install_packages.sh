#!/bin/bash

sudo pacman -Syu
sudo pacman -S --needed - < ~/.config/pkglist.txt
