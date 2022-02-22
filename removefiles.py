import time, os, shutil

source = input("Enter a path: ")
days = float(input("Enter the minimum number of days the file has existed for it to be deleted: "))
print(source)
if(not os.path.exists(source)):
   print("Path not found, try again")
else:
    print(source)
    currTime = time.time()
    fileList = os.listdir(source)
    for file in fileList:
        path = os.path.join(source, file)
        cTime = os.stat(path).st_ctime
        seconds = days * 24 * 60 * 60
        print(currTime - cTime)
        print(currTime - cTime > seconds)
        if (currTime - cTime) > seconds:
            os.remove(path)
        
        
