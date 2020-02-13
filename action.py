import os
str = os.environ['INPUT_SLOT']
print('input slot is {0:s}'.format(str))

print(os.listdir(os.getcwd()))

str = '0000'

if None != str:
    command = 'echo ::set-output name=result::{0:s}'.format(str)
    print(command)
    print(os.popen(command).read())

