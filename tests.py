#!/usr/bin/env python3
# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
from local_pip.colorama import init as coloramaInit, Fore as txtColor , Back as txtColorBack, Style as txtStyle
import utils.utility_belt as uBelt
import utils.utility_git as uGit
from utils.utility_config import BaseConfigger
from sys import argv as sys_argv, version as sys_version, exit as sys_exit
from string import ascii_lowercase
from os import linesep as os_linesep, path as os_path, remove as os_remove
from tempfile import gettempdir
### Python 2/3
try:
  from typing import List, Set, Dict, Tuple, Text, Optional
except:
  pass
#######################

class TestConfigClass(object):
  def __init__(self):
    self.enabled = True # type: bool
    self.lastByLines = [] # type: List[str]
    self.repoSrc = '' # type: str

  def __str__(self):
    return str(vars(self))


class TestConfigger(BaseConfigger) :
  def __init__(self):
    self.json_file_name = '.config.byLines.test.json' # type: str
    self.file_path_segments = [ gettempdir(), self.json_file_name ] # type: List[str]
    self.config_class = TestConfigClass() # type: TestConfigClass

def testBaseConfigger():
  testConfigger = TestConfigger()

  testConfigger.saveConfigClassToJson()
  assert testConfigger.doesConfigFileExist() is True
  os_remove(testConfigger.getFilePath())
  assert testConfigger.doesConfigFileExist() is False

  testConfigger.saveConfigClassToJson()
  testConfigger.config_class.enabled = False
  assert testConfigger.config_class.enabled is False
  testConfigger.loadJsonToConfigClass()
  assert testConfigger.config_class.enabled is True

  testConfigger.config_class.enabled = False
  testConfigger.saveConfigClassToJson()
  testConfigger.loadJsonToConfigClass()
  assert testConfigger.config_class.enabled is False

def testUtilityGit():
  top_level_dir = uGit.getGitTopLevelDir() 
  assert top_level_dir is not None
  path_to_test_file = os_path.join(top_level_dir, 'tests.py')
  assert os_path.exists(path_to_test_file)


if __name__ == "__main__":
  uBelt.log('Python Version:' + sys_version)
  args = sys_argv
  uBelt.log('ARGS:' + str(args))
  
  testUtilityGit()
  testBaseConfigger()

  uBelt.log('If you saw no errors above then the tests passed')




