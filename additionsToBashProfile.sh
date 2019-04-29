alias reload="source ~/.bash_profile"

function byLines() { command python ~/workspace/byLines/byLines.py "$@" }
function byLines3() { command python3 ~/workspace/byLines/byLines.py "$@" }

function git() { command git "$@" && python ~/workspace/byLines/byLines.py "$@" }
function git3() { command git "$@" && python3 ~/workspace/byLines/byLines.py "$@" }

function l() { ls -al $@ }