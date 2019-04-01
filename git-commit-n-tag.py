#!/usr/bin/env python3
# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
import utils.utility_belt as uBelt
import utils.utility_git as uGit
import utils.utility_config as uConfig
from sys import argv as sys_argv, version as sys_version
from string import ascii_lowercase
from os import linesep as os_linesep



def triggerTaggingFlow(config_dict, commit_hash):
  uBelt.log('triggerTaggingFlow() ' + commit_hash, isVerbose=True)
  selected_tags = []
  isFlowActive = True
  while(isFlowActive):
    print('¸.·´¯`·.¸><(((º>')
    print("Git Commit'n'Tag makes it easy to add 'n' tags to commit " + commit_hash)
    print('¸.·´¯`·.´¯`·.¸¸.·´¯`·.¸><(((º>')
    if len(selected_tags) > 0:
      print('')
      print('Tags currently staged to add to commit: ')
      print(selected_tags)
    
    optional_or = ''
    tags = sorted(config_dict['tags'])
    if len(tags) > 0:
      optional_or = 'or '
      print('')
      print('Enter the letter associated with a previosly used tag to add')
      abc_list = list(ascii_lowercase)
      for tag in tags:
        print('  ' + abc_list.pop(0) + ') ' + tag)
        print('')
    
    print(optional_or + 'write your own tag like: Your Name <your-git-email@github.com>')
    print('')
    selected_input = uBelt.getInput('Enter your selection [xx to exit]: ')

    if 'xx' == selected_input.lower():
      isFlowActive = False
    elif len(selected_input) < 3:
      tag_index = ascii_lowercase.find(selected_input.lower()[0])
      try:
        tag = tags[tag_index]
        selected_tags.append(tag)
      except IndexError:
        uBelt.log("Tag selection unknown, please try again or exit")
    else:
      config_dict["tags"].append(selected_input)
      selected_tags.append(selected_input)
  
  return config_dict, selected_tags


def addTagsToCommit(commit_hash, tags_to_add):
  uBelt.log('addTagsToCommit() ' + commit_hash + ': ' + str(tags_to_add))
  if len(tags_to_add) < 1:
    return
    
  commit_message = uGit.getGitCommitMessage(commit_hash)
  # Attempt to detect existing newline char
  if commit_message.find('\r\n'):
    new_line_character = '\r\n'
  elif commit_message.find('\n'):
    new_line_character = '\n'
  else:
    new_line_character = os_linesep

  # Attempt to detect if Author or Co
  if len(tags_to_add) > 1 or commit_message.lower().find('authored-by: ') > 1:
    tag_prefix = 'Co-authored-by: '
  else:
    tag_prefix = 'Authored-by: '

  # Add the tags to the message
  for tag in tags_to_add:
    prefix_with_tag = tag_prefix + tag
    if commit_message.find(prefix_with_tag) == -1:
      commit_message = commit_message + new_line_character + prefix_with_tag

  # Ammend the commit
  uBelt.IS_VERBOSE_LOGGING_ENABLED = True
  uGit.ammendCommitMessage(commit_message)



def main(args):
  config_dict = uConfig.getConfigJsonToDict()
  if config_dict['enabled'] is False:
    uBelt.log("Git Commit'n'Tag is disabled", isVerbose=True)
    return

  last_commit_hash = uGit.getGitCommitHash()
  if True or (uBelt.getCurrentTimeEpochMs() - uGit.getGitCommitEpochMs(last_commit_hash)) >= 10000:
    config_dict, selected_tags = triggerTaggingFlow(config_dict, last_commit_hash)
    uConfig.writeConfigDictToJson(config_dict, file_path=uConfig.getConfigFilePath())

    addTagsToCommit(last_commit_hash, selected_tags)



# uBelt.IS_VERBOSE_LOGGING_ENABLED = True
if __name__ == "__main__":
  uBelt.log('Python Version:' + sys_version, isVerbose=True)
  args = sys_argv
  uBelt.log('ARGS:' + str(args), isVerbose=True)

  if len(args) < 2:
    exit
  
  switch_arg = args[1].lower().strip()
  uBelt.log('SwitchArg:' + switch_arg, isVerbose=True)

  if 'commit' == switch_arg:
    main(args)
  if 'status' == switch_arg: # This may need to be removed
    main(args)



