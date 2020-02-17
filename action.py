#import machine
#machine.freq(160*1000*1000)
import fileinput
import os
import sys

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)
        
#frequency can only be either 80Mhz or 160MHz
freq_list = ['80', '160']
str = os.environ['INPUT_CPU']

if str in freq_list:
    print('set cpu to {0:s}MHz.'.format(str))
    print(os.listdir(os.getcwd()))
    mk_path = os.path.join(os.getcwd(), 'my_micropython', 'ports', 'esp8266', 'modules', 'inisetup.py')
    print(mk_path)
    replaceAll(mk_path, "#webrepl.start()","import machine;machine.freq({0:s}*1000*1000);#webrepl.start()".format(str))
    result = 'good!'
    with open(mk_path, 'r') as ff:
        print(ff.read())
else:
    result = 'bad!'
    print('frequency can only be either 80Mhz or 160MHz')

if None != str:
    command = 'echo ::set-output name=result::{0:s}'.format(result)
    print(command)
    print(os.popen(command).read())

