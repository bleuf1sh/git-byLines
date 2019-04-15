#!/usr/bin/env python3
# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
from local_pip.colorama import init as coloramaInit, Fore as txtColor , Back as txtColorBack, Style as txtStyle
import utils.utility_belt as uBelt
import utils.utility_git as uGit
import utils.utility_config as uConfig
from sys import argv as sys_argv, version as sys_version
from string import ascii_lowercase
from os import linesep as os_linesep



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


def triggerTaggingFlow(config_dict, commit_hash):
  coloramaInit()
  up_fish = '´¯`·.´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·><(((º>'
  dn_fish = '¸.·´¯`·.¸¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.><(((º>'
  sm_fish = '´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.><(((º>'

  uBelt.log('triggerTaggingFlow() ' + commit_hash, isVerbose=True)
  print(os_linesep + os_linesep + os_linesep)
  print('last commit:' + commit_hash)
  print(reset_colors())
  print(up_fish)
  print("Git Commit'n'Tag makes it easy to add N tags the most recent commit")
  print(dn_fish)
  
  selected_tags = []
  isFlowActive = True
  tags = sorted(config_dict['tags'])
  while(isFlowActive):
    select_tag_prompt = ''
    if len(tags) > 0:
      select_tag_prompt = 'Select a tag by letter or '
      print('Enter the letter to select a tag:')
      abc_list = list(ascii_lowercase)
      for tag in tags:
        if tag in selected_tags:
          print(reset_colors() + txtColor.LIGHTYELLOW_EX + txtStyle.BRIGHT + '  ✔' + ' (' + abc_list.pop(0) + ') ' + tag + os_linesep)
        else:
          print(reset_colors() + txtColor.LIGHTYELLOW_EX + txtStyle.NORMAL + '   ' + ' (' + abc_list.pop(0) + ') ' + tag + os_linesep)
    
    print(reset_colors() + select_tag_prompt + 'Write a new tag like ' + txtStyle.BRIGHT + 'Your Name <git-email@github.com>' + reset_colors())
    print(txtStyle.DIM + txtColor.BLACK + ':q quits  :a ammends commit' + os_linesep)
    selected_input = uBelt.getInput(reset_colors() + '-> ').strip()
    if '' == selected_input:
      continue 
    if ':q' == selected_input.lower():
      exit(0)
    if ':a' == selected_input.lower():
      isFlowActive = False
    elif len(selected_input) < 3:
      tag_index = ascii_lowercase.find(selected_input.lower()[0])
      try:
        tag = tags[tag_index]
        if tag in selected_tags:
          selected_tags.remove(tag)
        else:
          selected_tags.append(tag)
      except IndexError:
        show_warning('Tag selection unknown, please try again or exit')
    else:
      tags.append(selected_input)
      selected_tags.append(selected_input)
    
    print(sm_fish + os_linesep)
  
  # Update config with any newly added tags
  for selected_tag in selected_tags:
    if selected_tag not in config_dict["tags"]:
      config_dict["tags"].append(selected_tag)

  return config_dict, selected_tags


def addTagsToCommit(commit_hash, tags_to_add):
  uBelt.log('addTagsToCommit() ' + commit_hash + ': ' + str(tags_to_add), isVerbose=True)
  if len(tags_to_add) < 1:
    show_warning('No tags selected to ammend to commit')
    return
  
  ammended_commit_message = createAmmendedCommitMessage(commit_hash, tags_to_add)
  print(reset_colors() + txtStyle.BRIGHT + txtColor.WHITE)
  print('Commit message after ammendement:')
  print(reset_colors() + txtStyle.NORMAL + txtColor.LIGHTYELLOW_EX)

  print(ammended_commit_message)
  print(reset_colors())
  selected_input = uBelt.getInput('Confirm the ammended commit message above? [y/n]: ')
  if selected_input.lower().startswith('n'):
    show_warning('Ammend aborted')
    return

  # Ammend the commit
  uGit.ammendCommitMessage(ammended_commit_message)
  print('DONE')

def createAmmendedCommitMessage(commit_hash, tags_to_add):
  commit_message = uGit.getGitCommitMessage(commit_hash)
  # Attempt to detect existing newline char
  if commit_message.find('\r\n'):
    new_line_character = '\r\n'
  elif commit_message.find('\n'):
    new_line_character = '\n'
  else:
    new_line_character = os_linesep

  commit_message = commit_message + new_line_character

  # Attempt to detect if Author or Co
  if len(tags_to_add) > 1 or commit_message.lower().find('authored-by: ') > 1:
    tag_prefix = 'Co-authored-by: '
  else:
    tag_prefix = 'Authored-by: '

  # Add the tags to the message
  for tag in tags_to_add:
    prefix_with_tag = tag_prefix + tag
    if commit_message.find(tag) == -1:
      commit_message = commit_message + new_line_character + prefix_with_tag
  
  return commit_message


def reset_colors():
  return txtStyle.RESET_ALL + txtColorBack.BLUE + txtColor.WHITE

def show_warning(txt):
  uBelt.log(reset_colors() + txtColor.LIGHTRED_EX + '!!! ' + txt + ' !!!' + reset_colors())


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



