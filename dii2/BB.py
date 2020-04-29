def fin(n):
    L=[]
    i,a,b=0,0,1
    while i <n:
        L.append(b)
        a,b=b,a+b
        i+=1
    return L
def fin2(n):
    i,a,b=0,0,1
    while True:
        if n<=0 or i==n:
            break
    a,b=b,a+b
    yield a
    i+=1        
print(fin2(10))
