import os
str = os.environ['INPUT_IN_STR']
print('input is {0:s}'.format(str))

str = str.replace("-", "_");
str = str.replace(".", "_");

if None != str:
    command = 'echo ::set-output name=str::{0:s}'.format(str)
    print(command)
    print(os.popen(command).read())

