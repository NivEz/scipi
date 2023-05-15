#!/bin/bash


cwd=$(basename $(pwd))

if [ $cwd == "scipi" ]; then
  cd cli
else
  if [ $cwd == "scripts" ]; then
    cd ../cli
  else
    echo Execute from scipi directory
    exit 1
  fi
fi


# activate venv
source venv/bin/activate
python main.py
