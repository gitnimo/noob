import json 
fn='ABC.json'
with open(fn,'r',encoding='utf-8') as file:
    js=json.load(file)
    
    print(js['cwbopendata']['location'][0]['parameter'][2]['parameterName'])
