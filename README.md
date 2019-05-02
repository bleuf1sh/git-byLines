# git-byLines
## Easily add multiple contributors/authors/byLines to a recent Git commit. <br/>Simply *git commit* as usual... no extra commands to remember!

## Installation
Simply copy/paste this line into terminal (bash) and run to install
```
curl -sL "https://raw.githubusercontent.com/bleuf1sh/git-byLines/master/installByLines.sh?$(date +%s)" > installByLines.sh && bash installByLines.sh
```

![Demo](demo-images/demo_flow.png?raw=true "Demo")

## Usage
- Runs automatically after any  **git commit**  shell command
- Invoke directly with the  **byLines**  shell command

## Features
- Intelligently add contributors using the *Authored-by* or *Co-authored-by*<br/> syntax based on selection count or if an *Authored-by* is already present
- Prevents adding duplicate authors
- Ability to disable for an individual repo
- Remembers and Auto selects the previously used byLines
- Displays a preview before amending of the final commit message for confirmation
- Currently supports adding unlimited contributors
- Python 2 and 3 compatible
- Uses a local dependency folder to not clutter your global Python dependencies
- **byLine** can be safely run back-to-back in case someone was forgotten

## What makes this different than other approaches out there?
There are no specific commands to remember or configurations to setup before use.<br/>
The code is triggered upon any **git commit** command performed within any git repo.
Thereby achieving that natural flow similar to signing your name after writing an email.

## How does it work?
git-byLines overloads the git command via shell function and is triggered upon any **git commit** command. 
<br/>It can also be triggered manually via the shell function **byLines**.

A config file named `.config.byLines.json` is automatically generated inside of each repo and is recommended to be added to source control.

## Manual Install
1. Clone this repo to a directory of your choosing
1. Look at `additionsToBashProfile.sh` for examples of the functions to manually add (adapt) to your shell

## Requirements
- Python 2.7 and above
- Pip

## TODO
- Add auto-update ability
- Support for Fish shell
- Windows support
<br/>

## Inspired by
- https://github.com/pivotal/git-author
- https://github.com/kejadlen/git-together
- https://github.com/pivotal/git_scripts
- https://github.com/git-duet/git-duet

<br/><br/><br/><br/>
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
