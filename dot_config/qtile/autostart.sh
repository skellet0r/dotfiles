#!/bin/bash

# set background
nitrogen --restore &

# run xinitrc
sh $HOME/.xinitrc &

# start picom
picom &

# start dunst
dunst -transparency 30 &

# start xss-lock with xsecurelock as locker
xss-lock xsecurelock &

# graphical polkit agent
lxpolkit &
