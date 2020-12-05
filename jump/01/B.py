import xlwt
fn='hee.xls'
a=['name','num','birth','cmd']
b=['nimo','99','0125','']
A=xlwt.Workbook()
B=A.add_sheet('資料')
for i in range(len(a)):
    B.write(0,i,a[i])
for j in range(len(b)):
    B.write(1,j,b[j])
A.save(fn)