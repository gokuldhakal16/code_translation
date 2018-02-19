import os
#directory where the cloned RosettaCodeData is
dirname = "/home/gokul/RosettaCodeData/Task/"
#lists the directories
os.listdir(dirname)

import shutil
import errno
def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

count = 0
#cleanDirectory = input("Enter the directory name for processed data: ")
cleanDirectory = "CleanedRosettaCodeData"
if not os.path.exists(cleanDirectory):
    os.mkdir(cleanDirectory)
inputlang = input("Enter the source/input language of your choice: ")
outputlang = input("Enter the output/target language of your choice: ")
for f in os.listdir(dirname):
    dirnameone = dirname +f +"/"
    
    dirlist = os.listdir(dirnameone)
    if inputlang in dirlist and outputlang in dirlist :
        copy(dirnameone+inputlang+"/", cleanDirectory+"/"+inputlang+"/"+f)
        copy(dirnameone+outputlang+"/", cleanDirectory+"/"+outputlang+"/"+f)
        count += 1
        
print(count)
