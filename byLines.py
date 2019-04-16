#!/usr/bin/env python3
# coding: utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
from local_pip.colorama import init as coloramaInit, Fore as txtColor , Back as txtColorBack, Style as txtStyle
import utils.utility_belt as uBelt
import utils.utility_git as uGit
import utils.utility_config as uConfig
from sys import argv as sys_argv, version as sys_version, exit as sys_exit
from string import ascii_lowercase
from os import linesep as os_linesep



def main(args):
  config_dict = uConfig.getConfigJsonToDict()
  if config_dict['enabled'] is False:
    uBelt.log("git-byLines is disabled", isVerbose=True)
    return

  last_commit_hash = uGit.getGitCommitHash()
  # Run this all the time after each command trigger
  if True or (uBelt.getCurrentTimeEpochMs() - uGit.getGitCommitEpochMs(last_commit_hash)) >= 10000:
    config_dict, selected_bylines = triggerByLineWorkFlow(config_dict, last_commit_hash)
    
    uConfig.writeConfigDictToJson(config_dict, file_path=uConfig.getConfigFilePath())

    addByLineToCommit(last_commit_hash, selected_bylines)


def triggerByLineWorkFlow(config_dict, commit_hash):
  coloramaInit()
  up_fish = '´¯`·.´¯`·.¸¸.·´¯`·.¸¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·><(((º>'
  dn_fish = '¸.·´¯`·.¸¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.><(((º>'
  sm_fish = '´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.·´¯`·.¸.><(((º>'

  uBelt.log('triggerByLineWorkFlow() ' + commit_hash, isVerbose=True)
  print(os_linesep + os_linesep + os_linesep)
  print('last commit:' + commit_hash + reset_colors())
  print(os_linesep)
  print(up_fish)
  print("git-byLines makes it easy to add byLines to the most recent local commit")
  print(dn_fish)
  
  selected_bylines = []
  isFlowActive = True
  bylines = sorted(config_dict['byLines'])
  while(isFlowActive):
    select_byline_prompt = ''
    if len(bylines) > 0:
      select_byline_prompt = 'Select a byLine by letter or '
      print('Enter the letter to select a byLine:')
      abc_list = list(ascii_lowercase)
      for byline in bylines:
        if byline in selected_bylines:
          print(reset_colors() + txtColor.LIGHTYELLOW_EX + txtStyle.BRIGHT + '  ✔' + ' (' + abc_list.pop(0) + ') ' + byline + os_linesep)
        else:
          print(reset_colors() + txtColor.LIGHTYELLOW_EX + txtStyle.NORMAL + '   ' + ' (' + abc_list.pop(0) + ') ' + byline + os_linesep)
    
    print(reset_colors() + select_byline_prompt + 'Write a new byLine like ' + txtStyle.BRIGHT + 'Your Name <git-email@github.com>')
    print(reset_colors() + txtStyle.DIM + txtColor.BLACK + ':q quits  :a ammends commit' + os_linesep)
    selected_input = uBelt.getInput(reset_colors() + '-> ').strip()
    if '' == selected_input:
      continue 
    if ':q' == selected_input.lower():
      sys_exit(0)
    if ':a' == selected_input.lower():
      isFlowActive = False
    elif len(selected_input) < 3:
      tag_index = ascii_lowercase.find(selected_input.lower()[0])
      try:
        byline = bylines[tag_index]
        if byline in selected_bylines:
          selected_bylines.remove(byline)
        else:
          selected_bylines.append(byline)
      except IndexError:
        show_warning('byLine selection unknown, please try again or exit')
    else:
      bylines.append(selected_input)
      selected_bylines.append(selected_input)
    
    print(sm_fish + os_linesep)
  
  # Update config with any newly added byLines
  for selected_byline in selected_bylines:
    if selected_byline not in config_dict["byLines"]:
      config_dict["byLines"].append(selected_byline)

  return config_dict, selected_bylines


def addByLineToCommit(commit_hash, bylines_to_add):
  uBelt.log('addByLineToCommit() ' + commit_hash + ': ' + str(bylines_to_add), isVerbose=True)
  if len(bylines_to_add) < 1:
    show_warning('No byLines selected to ammend to commit')
    return
  
  ammended_commit_message = createAmmendedCommitMessage(commit_hash, bylines_to_add)
  print(reset_colors() + txtColor.WHITE)
  print('Commit message after ammendement:')
  print(reset_colors() + txtColor.LIGHTYELLOW_EX)

  print(ammended_commit_message)
  print(reset_colors())
  selected_input = uBelt.getInput('Confirm the ammended commit message above? [y/n]: ')
  if selected_input.lower().startswith('n'):
    show_warning('Ammend aborted')
    return

  # Ammend the commit
  uGit.ammendCommitMessage(ammended_commit_message)
  print('DONE')

def createAmmendedCommitMessage(commit_hash, bylines_to_add):
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
  if len(bylines_to_add) > 1 or commit_message.lower().find('authored-by: ') > 1:
    byline_prefix = 'Co-authored-by: '
  else:
    byline_prefix = 'Authored-by: '

  # Add the byLines to the message
  for byline in bylines_to_add:
    prefix_with_tag = byline_prefix + byline
    if commit_message.find(byline) == -1:
      commit_message = commit_message + new_line_character + prefix_with_tag
  
  return commit_message


def reset_colors():
  return txtStyle.NORMAL + txtColorBack.BLUE + txtColor.WHITE

def show_warning(txt):
  uBelt.log(reset_colors() + txtColor.LIGHTRED_EX + '!!! ' + txt + ' !!!' + reset_colors())


if __name__ == "__main__":
  uBelt.log('Python Version:' + sys_version, isVerbose=True)
  args = sys_argv
  uBelt.log('ARGS:' + str(args), isVerbose=True)
  
  if len(args) >= 2:
    switch_arg = args[1].lower().strip()
    uBelt.log('SwitchArg:' + switch_arg, isVerbose=True)

    if 'commit' == switch_arg:
      main(args)
  
  else:
    main(args)




