import os
cur_path=os.path.dirname(__file__) #取得目前路徑
os.system("cls") # 清除螢幕
os.system("mkdir dir2")#建立dir2目錄
os.system("copy sd.py dir2\copyfile.py") #複製檔案
file=cur_path+"\dir2\copyfile.py"
os.system("notepad"+file)#以記事本開啟檔案