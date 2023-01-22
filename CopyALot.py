#function for copying a lot of files

import os
import shutil

def copylott(src, dst):
    for i in os.listdir(src):
        shutil.copy2(src + i, dst)


source = '/home/hasu/Downloads/AI_Intro/Introduction_to_AI-main/ML/'
destination = '/home/hasu/Downloads/AI_Intro/Introduction_to_AI-main/CP/'
copylott(source, destination)
