#設計一個點餐系統 a=[客人點的餐點] b=[服務過的餐點] 
def Mc(a,b):
    print("客人點的餐點")
    while a:
        c=a.pop()
        print('菜單:',c)
        b.append(c)
def ki(a):
    print("尚未上的餐點")
    if not a:
        print("還沒有餐點")
    for A in a:
        print(A)

def ko(b):
    print('已經上的餐點')
    if not b:
        print('還沒有餐點已經完成') 
    for B in b:
        print(B)   

a=['生魚片','雞塊','燒餅','可口可樂']
b=[]
ki(a)
ko(b)



        
        

