import math
class ps():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        temp=math.gcd(self.x,self.y)
        tuso = self.x/temp
        mauso = self.y/temp
        return '{0}/{1}'.format(int(tuso),int(mauso))
    def __add__(self,PS):
        mauso = self.y*PS.y
        tuso=self.x*PS.x+self.y*PS.y
        return ps(tuso,mauso)
    def hieu(self,PS):
        mauso=self.y*PS.y
        tuso=self.x*PS.x-self.y*PS.y
        return ps(tuso,mauso)
    def tich(self,PS):
        mauso=self.y*PS.y
        tuso=self.x*PS.x
        return ps(tuso,mauso)
    def thuong(self,PS):
        mauso=self.y*PS.x
        tuso=self.x*PS.y
        return ps(tuso,mauso)
ps1 = ps(1,2)
ps2 = ps(2,4)
print(ps1+ps2)
print(ps1.hieu(ps2))
print(ps1.tich(ps2))
print(ps1.thuong(ps2))