alias reload="source ~/.bash_profile"
function l() { ls -al $@ ; }

# Add for direct invocation ability (needed for git overload)
# Note the different Pythons... pick the one that matches appropriately with your python
function byLines() { command python ~/workspace/byLines/byLines.py "$@" ; }
function byLines() { command python3 ~/workspace/byLines/byLines.py "$@" ; }

# Add for Git overload
function git() { command git "$@" && byLine "$@" ; }