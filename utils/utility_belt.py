from __future__ import absolute_import, division, print_function, unicode_literals
from time import time
from subprocess import check_output
from os import system, name
from re import compile as re_compile
### Python 2/3
try:
  from typing import List, Set, Dict, Tuple, Text, Optional
except:
  pass
#######################
### Python 2/3
try:
    input = raw_input # type: ignore # Added for 2.X compatibility
except NameError:
    pass
#######################

IS_VERBOSE_LOGGING_ENABLED = False
ANSI_ESCAPED_REGEX = re_compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')

def log(text, isVerbose=False):
  # type: (str, bool) -> None
  if IS_VERBOSE_LOGGING_ENABLED or isVerbose is False:
    print(text)

def getInput(message, defaultValue=''):
  # type: (str, str) -> str
  user_input = input(message)
  return safeCast(user_input, str, defaultValue)

def getCurrentTimeEpochMs():
  # type: () -> int
  return int(round(time() * 1000))

def safeCast(val, to_type, default=None):
  try:
    return to_type(val)
  except (ValueError, TypeError) as e:
    log(e)
    return default

def ansi_strip(text):
  # type: (str) -> str
  return ANSI_ESCAPED_REGEX.sub('', text)

def getOutputExecutingShellCommands(shell_commands):
  # type: (List[str]) -> str
  raw_output = check_output(shell_commands).decode('utf-8')

  cleaned_output = safeCast(raw_output, str, '')
  if cleaned_output.startswith('"'):
    cleaned_output = cleaned_output[1:]
  if cleaned_output.endswith('"'):
    cleaned_output = cleaned_output[:-1]

  return cleaned_output.strip()


def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 