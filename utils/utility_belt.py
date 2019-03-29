from __future__ import absolute_import, division, print_function, unicode_literals
import time
import subprocess

IS_VERBOSE_LOGGING_ENABLED = False

def log(text, isVerbose=False):
  if IS_VERBOSE_LOGGING_ENABLED or isVerbose is False:
    print(text)

def getCurrentTimeEpochMs():
  return int(round(time.time() * 1000))

def safeCast(val, to_type, default=None):
  try:
    return to_type(val)
  except (ValueError, TypeError) as e:
    log(e)
    return default

def getOutputExecutingShellCommands(shell_commands):
  raw_output = subprocess.check_output(shell_commands).decode('utf-8')

  cleaned_output = safeCast(raw_output, str, '')
  if cleaned_output.startswith('"'):
    cleaned_output = cleaned_output[1:]
  if cleaned_output.endswith('"'):
    cleaned_output = cleaned_output[:-1]

  return cleaned_output.strip()

