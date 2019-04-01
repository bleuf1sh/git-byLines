from __future__ import absolute_import, division, print_function, unicode_literals
import utils.utility_belt as uBelt

def ammendCommitMessage(new_commit_message):
  output = uBelt.getOutputExecutingShellCommands(['git', 'commit', '--amend', '-m "' + new_commit_message + '"'])
  uBelt.log('ammendCommitMessage() got:' + output, isVerbose=True)
  return output

def getGitTopLevelDir():
  output = uBelt.getOutputExecutingShellCommands(['git', 'rev-parse', '--show-toplevel'])
  uBelt.log('getGitTopLevelDir() got:' + output, isVerbose=True)
  return output

def getGitCommitPrettyArg(pretty_format_args, specific_git_hash=None):
  shell_command = ['git', 'log', '-n 1', '--pretty=format:"' + pretty_format_args + '"']
  if specific_git_hash is not None:
    shell_command.append(specific_git_hash)

  output = uBelt.getOutputExecutingShellCommands(shell_command)
  return output

def getGitCommitHash():
  return getGitCommitPrettyArg('%H')

def getGitCommitEpochMs(specific_git_hash=None):
  result = getGitCommitPrettyArg('%ct', specific_git_hash)
  return uBelt.safeCast(result, int, 0)

def getGitCommitMessage(specific_git_hash=None):
  return getGitCommitPrettyArg('%B', specific_git_hash)

