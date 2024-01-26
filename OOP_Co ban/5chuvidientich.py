class DaGiac:
    def __init__(self,socanh):
        self.n=socanh
        self.canh=[0 for i in range(socanh)]
    def nhap(self):
        self.canh= [float(input()) for i in range(self.n)]
    def show(self):
        for i in range(self.n):
            print(self.canh[i])
class TamGiac(DaGiac):
    def __init__(self):
        DaGiac.__init__(self,3)
    def dientich(self):
        a,b,c = self.canh
        s=(a+b+c)/2
        area =(s*(s-a)*(s-b)*(s-c))**0.5
        print(f'{area:.2f}')
t=TamGiac()
t.nhap()
t.show()
t.dientich()