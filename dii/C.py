import os.path
os.path.abspath()# 傳回檔案完整的路徑名稱
os.path.basename()#傳回檔案路徑名稱最後的檔案或路徑名稱。如果測試的是檔案會傳回黨名，測試的是路徑會傳回路徑。
os.path.dirname()#傳回指定檔案完整的目錄路徑，dirname(__file__)則可以取得目前的目錄路徑
os.path.exists()#檢查指定的檔案或路徑是否存在
os.path.getsize()#取得指定檔案的大小
os.path.isabs()#檢查指定路徑是否完整路徑名稱
os.path.isfile()#檢查指定路徑是否為檔案
os.path.isdir()#檢查指定路徑是否為目錄
os.path.split()#分割檔岸路名稱為目錄路徑和檔案
os.path.splitdrive()#分割檔案路徑名稱為磁碟機和檔案路徑名稱
os.path.join()#將路徑和檔案名稱結合為完整的路徑