#copyfile() = copies contents of a file
#copy()= copyfile() +permission+destination can be a directory
#copy2()= copy() +copies metadata

import shutil

shutil.copy2('test.txt','copy.txt') #src.dst