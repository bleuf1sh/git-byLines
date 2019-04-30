alias reload="source ~/.bash_profile"
function l() { ls -al $@ ; }

# Note the different Pythons
function byLines() { command python ~/workspace/byLines/byLines.py "$@" ; }
function byLines() { command python3 ~/workspace/byLines/byLines.py "$@" ; }

function git() { command git "$@" && byLine "$@" ; }