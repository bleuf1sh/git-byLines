alias reload="source ~/.bash_profile"

function l() {
    ls -al $@
}
function git() {
    # TODO: add so only triggers python code when second param is "commit"
    command git "$@" && python ~/git-autograph.py "$@"
}
function git3() {
    # TODO: add so only triggers python code when second param is "commit"
    command git $@ && python3 ~/git-autograph.py "$@"
}