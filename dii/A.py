import os          

dir="mydir"
if  os.path.exists(dir):  #檢查是否已存在
    os.rmdir(dir)
else:
    print(dir+"尚未建立")  #刪除目錄
import os 
dir="mydir"
if not os.path.exists(dir):
    os.mkdir(dir)
else:
    print(dir+"已經建立")   #建立目錄
import os
file="myfile.txt"
if os.path.exists(dir):
    os.remove(file)
else:
    print(file+"檔案尚未建立")#刪除檔案
