#!/bin/bash
#A nice addition to my bashrc adding the current git branch with colour to the CLI
#
#

# Git branch in prompt.
parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
green="\[\033[32m\]"
export PS1="\w\[$green\]\$(parse_git_branch)\[\033[00m\] $ "


# Explanation
# git branch 2>: Shows branches in current directory and outputs any 
# potential erros to /dev/null, basicaly ignoring them
#
# sed -e '/^[^*]/d': A sed command to delete all lines not starting with *
# effectively ignoring the other potential braches, we only want the current
# /: separates the command from the pattern and replacement
# ^: matches beginning of a line
# [^*]: regular expression that mathces any character except *
# /d: sed delete command, any line matching the pattern is deleted
#
# -e 's/* \(.*\)/ (\1)/': A substitution command to match any character and wrap it in parentheses. 
# s/: substitution command
# \(.*\): capturing group
# .*: matchs any sequence of characters except newline characters
# (\1): replacement part, wrap what was captured, i.e. \1 and wrap it in ()
#
# -e signifies multiple expressions in the same sed command
#
# "\[\033[32m\]": ANSI escape code in bash scripting and used to control formatting colours.
# \[\003: starts the sequence
# 32m: green colour in ANSI colour code
# \] end of escape sequence
#
#
# # The export statement
# PS1= Sets the PS1 environment variable which determines the format of the bash prompt
# \w: represents the current working directory
# \[$green\]: set the colour as green
# call the function to return the branch in green colour wrapped in ()
# \[033[00m\]: resets the text colour
# $ ": indicates the prompt is ready to accept commands
