import time
import os
import shutil

path = input("Enter the path: ")
days = int(input("Enter the number of days: ")) * 86400
timeLimit = time.time() - days
if os.path.exists(path):
    for currentPath, directories, files in os.walk(path):
        for i in directories:
            folderPath = os.path.join(currentPath, i)
            folderctime = os.stat(folderPath).st_ctime
            if folderctime < timeLimit:
                shutil.rmtree(folderPath)
        for j in files:
            filePath = os.path.join(currentPath, j)
            filectime = os.stat(filePath).st_ctime
            if filectime < timeLimit:
                os.remove(filePath)
else:
    print("This path is not found!")
