import re
msg="howhow 0963-057-002 0963-057-002 0963-057-002"
msg1="我是一隻小小鳥"
msg3="09333336650963-057-002"
def PHONE(st):
    phone=re.compile(r'{4d}-\d\d\d-\d\d\d')
    phonenum=phone.findall(st)
    if phonenum!= None:
        print(phonenum)
    
PHONE(msg)
PHONE(msg1)
PHONE(msg3)