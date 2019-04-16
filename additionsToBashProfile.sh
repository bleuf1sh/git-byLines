alias reload="source ~/.bash_profile"

function l() {
    ls -al $@
}
function byLines() {
    command python ~/workspace/byLines/byLines.py "$@"
}
function git() {
    # TODO: add so only triggers python code when second param is "commit"
    command git "$@" && python ~/workspace/byLines/byLines.py "$@"
}
function git3() {
    # TODO: add so only triggers python code when second param is "commit"
    command git "$@" && python3 ~/workspace/byLines/byLines.py "$@"
}