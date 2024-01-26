import math
class ps():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        temp = math.gcd(self.x,self.y)
        tuso = self.x/temp
        mauso = self.y/temp
        return '{0}/{1}'.format(int(tuso),int(mauso))
    def __add__(self,PS):
        mauso = self.y*PS.y 
        tuso = self.x*PS.y+self.y*PS.x
        return ps(tuso,mauso)
if __name__ == '__main__':
    ps1 = ps(2,3)
    ps2 = ps(2,4)
    print(ps1+ps2)