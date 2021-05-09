#!/bin/bash

# set background
nitrogen --restore &

# start picom
picom &

# start dunst
dunst -transparency 30 &

# start xss-lock with xsecurelock as locker
xss-lock xsecurelock &

# graphical polkit agent
lxpolkit &

# run xinitrc
sh ~/.xinitrc &

