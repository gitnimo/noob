b=int(input("number:"))
i=2
L=[]
for i in range(2,b+1):
    k=2
    for k in range(2,i):
        if i%k==0:
            break
    else:
        L.append(i)
print(L)
        

    
     
     