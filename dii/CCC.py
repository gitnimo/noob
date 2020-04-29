class Myschool():
    def __init__(self,uname):
        self.name=uname
        self.score=0
        self.title="python school"
    def save_fun(self,fun):
        self.score += fun
        print(self.title.title(),'\n',self.name.title()+"的成績是",fun,"分")

b=Myschool('lee')
b.save_fun(80)             ###12-29習題