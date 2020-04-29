class Banks():                 ###習題12-29
    def __init__(self,uname): 
        self.name=uname
        self.blanse=0
        self.title="nimo bank"
    def save_money(self,money):
        self.blanse += money
        print("存款",money,"元")
    def withdraw(self,money):
        self.blanse-=money
        print("提款",money,"元")
    def showblanse (self):
        print("目前餘額:",self.blanse)

nimoo= Banks('nimoo')
nimoo.save_money(5000)
nimoo.withdraw(3000)
nimoo.save_money(1500)
nimoo.showblanse()  
