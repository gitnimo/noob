import csv
fn='0_04.csv'


with open("C:/Users/Nimo/Desktop/sd/0_04.csv",'w',newline='') as file:
    o=['sada','sada','sa']
    s=csv.DictWriter(file,fieldnames=o)
    s.writeheader()
    s.writerow({'sada':'sada','sada':'sss','sa':'sad'})
    

    