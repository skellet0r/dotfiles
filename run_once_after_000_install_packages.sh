#!/bin/bash

sudo pacman -Syu --noconfirm
sudo pacman -S --needed --noconfirm - < ~/.config/pkglist.txt
