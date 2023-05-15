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

chmod +x ../scripts/scipi.sh

echo "[] Creating Python virtual environment"
python -m venv venv

source venv/bin/activate

echo -e "[] Installing Python requirements\n"
pip install -r requirements.txt

echo -e "\n[] Finished setting up - SciPi is ready for use"
