# git-byLines
## Simple Git tool to ammend contributers onto a commit message requiring no special commands
copy/paste this line into terminal (bash) and run
```
TODO... for later
```


## What makes this different than other approaches out there?
There are no specific commands to remember or configurations to setup before use. 
The code is triggered upon any **git commit** command within any git repo.

## How does it work?
git-byLines overloads the git command via shell alias and is triggered upon any **git commit** command. 
It can also be triggered manually via the shell alias **byLines**.

A config file named **.config.byLines.json** is automatically generated inside of each repo and can be safely added to source control.


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
