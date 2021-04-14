# remove default fish greeting
set -g fish_greeting

# pyenv configuration
set -x PATH ~/.pyenv/bin $PATH
status --is-interactive; and . (pyenv init -|psub)
status --is-interactive; and . (pyenv virtualenv-init -|psub)

alias ls='exa --all --group-directories-first --long --group'
