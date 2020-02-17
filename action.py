#import machine
#machine.freq(240*1000*1000)
import fileinput
import os
import sys

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)
        
str = os.environ['INPUT_CPU']
print('set cpu to {0:s}MHz.'.format(str))
print(os.listdir(os.getcwd()))

mk_path = os.path.join(os.getcwd(), 'my_micropython', 'ports', 'esp32', 'modules', 'inisetup.py')
print(mk_path)
replaceAll(mk_path, "#webrepl.start()","import machine;machine.freq(240*1000*1000);#webrepl.start()")

if None != str:
    command = 'echo ::set-output name=result::{0:s}'.format(str)
    print(command)
    print(os.popen(command).read())

