#!/bin/bash
# auther: ccccmagicboy 
# url: ccrobot-online.com

#echo hello the world!
#echo $INPUT_TEST
# echo TZ="$INPUT_TZ1/$INPUT_TZ2"
# sudo timedatectl set-timezone $INPUT_TZ1/$INPUT_TZ2
# echo "::set-output name=datetime::$(date +'%Y%m%d_%H%M%S')"

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
#echo $SCRIPTPATH

python -m pip install --upgrade pip
#pip install -U pytz
#echo $(pwd)
python $SCRIPTPATH/action.py

#echo bye bye!
#echo "::set-output name=test_out::aaaabbbbcccc"
#echo "::set-output name=hash_v3::v33333"
#echo "::set-output name=hash_v4::v44444"


