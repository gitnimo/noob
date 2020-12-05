import xmltodict
fn='ABC.xml'
with open(fn,encoding='utf-8') as file:
    txt=xmltodict.parse(file.read())
    a=txt['cwbopendata']['location'][0]['weatherElement'][11]['elementValue']['value']
    print(a)