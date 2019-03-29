#!/usr/bin/env python3
from __future__ import absolute_import, division, print_function, unicode_literals
import utils.utility_belt as uBelt
import utils.utility_git as uGit
import sys
import os.path

### Python 2/3
try:
    input = raw_input
except NameError:
    pass
try:
  import simplejson as json
except (ImportError, SyntaxError):
  import json
#######################

uBelt.IS_VERBOSE_LOGGING_ENABLED = True

COMMIT_N_TAG_CONFIG_JSON_FILE_NAME = 'commit-n-tag.config.json'

COMMIT_N_TAG_CONFIG_DICT_STARTER = dict(
  enabled=True,
  tags=[ ]
)

def getConfigFilePath(repo_level=True):
  return os.path.join(uGit.getGitTopLevelDir(), COMMIT_N_TAG_CONFIG_JSON_FILE_NAME)

def doesConfigFileExist(repo_level=True):
  return os.path.isfile(getConfigFilePath())

def writeConfigDictToJson(config_dict, file=None, file_path=None):
  if file is None and file_path is None:
    raise ValueError('writeConfigDictToJson() Missing Required field: "file" or "file_path" must be provided')

  if file is not None:
    json.dump(config_dict, fp=file, indent=2)
  else:
    with open(getConfigFilePath(), mode='w') as autograph_config_json_file:
      uBelt.log('writeConfigDictToJson... Preparing Json')
      json.dump(config_dict, fp=autograph_config_json_file, indent=2)
      uBelt.log('writeConfigDictToJson... Wrote Json')

def getConfigJsonToDict(repo_level=True):
  config_file_path = getConfigFilePath()
  uBelt.log('getConfigJsonToDict... Loading Dict from:' + config_file_path, isVerbose=True)

  config_dict = None
  try:
    with open(config_file_path, mode='r') as config_json_file:
      config_dict = json.load(config_json_file)
      uBelt.log('getConfigJsonToDict... Loaded Dict', isVerbose=True)
  except Exception:
    config_dict = None
  
  if config_dict is None:
    uBelt.log('getConfigJsonToDict... No Dict Found', isVerbose=True)
    config_dict = COMMIT_N_TAG_CONFIG_DICT_STARTER.copy()
    writeConfigDictToJson(config_dict, file_path=config_file_path)
    os.chmod(config_file_path, 0o777)
    uBelt.log('getConfigJsonToDict... Creating Dict Done', isVerbose=True)

  return config_dict


def promptToAddTagToConfig():
  print('Tags look like "Your Name <your-git-email@github.com>"')
  incoming = input('Enter a new tag: ')
  return str(incoming)

def triggerTaggingFlow(commit_hash):
  uBelt.log('triggerTaggingFlow() ' + commit_hash, isVerbose=True)
  # while(True):


def main(args):
  config_dict = getConfigJsonToDict()
  last_commit_hash = uGit.getGitCommitHash()
  # if (uBelt.getCurrentTimeEpochMs() - uGit.getGitCommitEpochMs(last_commit_hash)) >= 10000:
  #   triggerTaggingFlow(last_commit_hash)

  uBelt.log(last_commit_hash)
  uBelt.log(uGit.getGitCommitHash())
  uBelt.log(uGit.getGitCommitEpochMs(last_commit_hash))
  uBelt.log(uGit.getGitCommitMessage(last_commit_hash))




if __name__ == "__main__":
  uBelt.log('Python Version:' + sys.version, isVerbose=True)
  args = sys.argv
  uBelt.log('ARGS:' + str(args), isVerbose=True)

  if len(args) < 2:
    exit
  
  switch_arg = args[1].lower().strip()
  uBelt.log('SwitchArg:' + switch_arg, isVerbose=True)

  if 'commit' is switch_arg:
    main(args)
  if 'status' is switch_arg:
    main(args)








######## BACKLOG ##########
# Quick option for most recently used autographs (specific to the machine)