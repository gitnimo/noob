import json
hero={"pyhon":\
     [{"日本":"hero"},\
      {"台灣":"banana"}]\
      }
fn='fin.json'
with open(fn,'w',encoding='utf-8') as file:
    json.dump(hero,file,ensure_ascii=False)
#python轉換json
#寫入json中文

import json
fn='fin.json'
with open (fn,'r',encoding='utf-8') as puppy:
    data=json.load(puppy)
print(data)
#json轉換python
##讀取中文 json
    