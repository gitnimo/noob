#import json
#fn='hero.json'
#login=input("請輸入帳號:")
#with open(fn,'w') as file:
    #json.dump(login,file)
    #print("%s歡迎來到此系統"%(login)) 
    #寫入帳號
#import json 
#fn='fin.json'
#with open (fn,'r') as file:
    #login=json.load(file)
    #print("%s歡迎再回來"%login)
import json 
fn='hero.json'

try:
    with open(fn,'r') as file:
        my=json.load(file)
except :
        my=input("請輸入帳號:")
        with open(fn,'w') as fut:
            json.dump(my,fut)
            print("%s歡迎第一次來到伺服器"%my)
else:
    print("%swelcomeback"%my)
    

    
