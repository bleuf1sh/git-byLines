from __future__ import absolute_import, division, print_function, unicode_literals
import utils.utility_belt as uBelt
from os import path as os_path, chmod as os_chmod, linesep as os_linesep
### Python 2/3
try:
  from typing import List, Set, Dict, Tuple, Text, Optional
except:
  pass
#######################
### Python 2/3
try:
  import simplejson as json
except (ImportError, SyntaxError):
  import json # type: ignore # Added for 2.X compatibility
#######################

class BaseConfigger(object):
  def __init__(self):
    self.json_file_name = None # type: str
    self.file_path_segments = None # type: List[str]
    self.config_class = None
  
  def getFilePath(self):
    return os_path.join(*self.file_path_segments) # * unpacks list to args

  def doesConfigFileExist(self):
    # type: (BaseConfigger) -> bool
    return os_path.isfile(self.getFilePath())

  def saveConfigClassToJson(self):
    with open(self.getFilePath(), mode='w') as config_class_json_file:
      uBelt.log('writeConfigClassToJson... Preparing Json', isVerbose=True)
      json.dump(vars(self.config_class), fp=config_class_json_file, indent=2)
      uBelt.log('writeConfigClassToJson... Wrote Json', isVerbose=True)

    try:
      os_chmod(self.getFilePath(), 0o755)
    except Exception as e:
      uBelt.log('writeConfigClassToJson...' + str(e), isVerbose=True)

  def loadJsonToConfigClass(self):
    # type: (BaseConfigger) -> bool
    uBelt.log('readJsonToConfigClass... Loading Json from:' + self.getFilePath(), isVerbose=True)
    try:
      with open(self.getFilePath(), mode='r') as config_class_json_file:
        loaded_dict = json.load(config_class_json_file)
        self.config_class.__dict__ = loaded_dict
        uBelt.log('readJsonToConfigClass... Loaded ConfigClass', isVerbose=True)
        return True
    except Exception as e:
      uBelt.log('readJsonToConfigClass...' + str(e), isVerbose=True)
      return False

  def __str__(self):
    dict_version_of_self = vars(self)
    dict_version_of_self['config_class'] = vars(self.config_class)
    return json.dumps(dict_version_of_self, indent=2)


