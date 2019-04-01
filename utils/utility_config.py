from __future__ import absolute_import, division, print_function, unicode_literals
import utils.utility_belt as uBelt
import utils.utility_git as uGit
from os import path as os_path, chmod as os_chmod
### Python 2/3
try:
  import simplejson as json
except (ImportError, SyntaxError):
  import json
#######################

COMMIT_N_TAG_CONFIG_JSON_FILE_NAME = 'commit-n-tag.config.json'

COMMIT_N_TAG_CONFIG_DICT_STARTER = dict(
  enabled=True,
  tags=[ ]
)


def getConfigFilePath(repo_level=True):
  return os_path.join(uGit.getGitTopLevelDir(), COMMIT_N_TAG_CONFIG_JSON_FILE_NAME)

def doesConfigFileExist(repo_level=True):
  return os_path.isfile(getConfigFilePath())

def writeConfigDictToJson(config_dict, file=None, file_path=None):
  if file is None and file_path is None:
    raise ValueError('writeConfigDictToJson() Missing Required field: "file" or "file_path" must be provided')

  if file is not None:
    json.dump(config_dict, fp=file, indent=2)
  else:
    with open(getConfigFilePath(), mode='w') as autograph_config_json_file:
      uBelt.log('writeConfigDictToJson... Preparing Json', isVerbose=True)
      json.dump(config_dict, fp=autograph_config_json_file, indent=2)
      uBelt.log('writeConfigDictToJson... Wrote Json', isVerbose=True)

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
    os_chmod(config_file_path, 0o777)
    uBelt.log('getConfigJsonToDict... Creating Dict Done', isVerbose=True)

  return config_dict