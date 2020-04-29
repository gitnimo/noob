def hook(k):
    L=[]
    for i in range(2,k+1):
        for j in range(2,i):
            if i%j ==0:
               break
        else:
            L.append(i)
    return L
            
print(hook(8))