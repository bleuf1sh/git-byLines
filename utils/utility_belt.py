from __future__ import absolute_import, division, print_function, unicode_literals
from time import time
from subprocess import check_output
from os import system, name
### Python 2/3
try:
    input = raw_input
except NameError:
    pass
#######################


IS_VERBOSE_LOGGING_ENABLED = False

def log(text, isVerbose=False):
  if IS_VERBOSE_LOGGING_ENABLED or isVerbose is False:
    print(text)

def getInput(message, defaultValue=''):
  user_input = input(message)
  return safeCast(user_input, str, defaultValue)

def getCurrentTimeEpochMs():
  return int(round(time() * 1000))

def safeCast(val, to_type, default=None):
  try:
    return to_type(val)
  except (ValueError, TypeError) as e:
    log(e)
    return default

def getOutputExecutingShellCommands(shell_commands):
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