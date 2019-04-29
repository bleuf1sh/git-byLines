# git-byLines
## Addon to ammend mulitple contributers <br/>onto a commit message **git commit** as usual <br/>no hard to remember commands... it's that simple!

copy/paste this line into terminal (bash) and run
```
curl -sL "https://raw.githubusercontent.com/bleuf1sh/git-byLines/master/installByLines.sh?$(date +%s)" > installByLines.sh && bash installByLines.sh
```


## What makes this different than other approaches out there?
There are no specific commands to remember or configurations to setup before use. 
The code is triggered upon any **git commit** command performed within any git repo.

## How does it work?
git-byLines overloads the git command via shell function and is triggered upon any **git commit** command. 
It can also be triggered manually via the shell function **byLines**.

A config file named `.config.byLines.json` is automatically generated inside of each repo and is reccomended to be added to source control.

## Manual Install
1. Clone this repo do a directory of your choosing
1. Look at `additionsToBashProfile.sh` for examples of the aliases to manually add to your shell

</br>

## Inspired by
- https://github.com/pivotal/git-author
- https://github.com/kejadlen/git-together
- https://github.com/pivotal/git_scripts
- https://github.com/git-duet/git-duet
</br></br>


######## BACKLOG ##########
- Update ReadMe

</br></br></br></br>
```
# MIT License

# Copyright (c) 2019 Aaron

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
```
