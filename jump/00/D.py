#import csv
#fn='eiv010.csv'
#with open(fn) as file:
#    csvr=csv.reader(file)
 #   csvl=list(csvr)
#print(csvl[1][0])
#reader 串列 迴圈方法打開

#import csv 
#fn='0_01.csv'
#with open(fn,'w') as file:
    #csvWriter=csv.writer(file)
    #csvWriter.writerow(['name','age','tall'])
    #csvWriter.writerow(['nimo','22','182'])
    #csvWriter.writerow(['joker','25','181'])
#寫入csv

#import csv 
#fn=' 0_01.csv'
#fn2='0_02.csv'
#with open(fn,'r') as file:
    #csvr=csv.reader(file)
    #csvrl=list(csvr)
#with open(fn2,'w',newline='')as file2:
   # csr=csv.writer(file2)
    #for row in csvrl:
    #    csr.writerow(row)
#複製csv

    
import csv
fn3='0_03.csv'
with open(fn3,'w') as file:
    csc=['Name','Age','Home']
    f3w=csv.DictWriter(file,fieldnames=csc)
    f3w.writeheader()#寫入標題 csc
    f3w.writerow({'Name':'chiami','Age':'23','Home':'yes'})
    f3w.writerow({'Name':'dan','Age':'25','Home':'no'})



    

   
