#!/bin/bash

function install() {
  local python_ref=""
  if [ $(which python3) ]; then
    local python_ref="python3"
  elif [ $(which python) ]; then
    local python_ref="python"
  fi
  
  echo "Found Python Ref:$python_ref"
}

install