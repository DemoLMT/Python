'''class hcn:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def __str__(self):
        return "Chieu dai: {0}\nChieu rong: {1}\nChu vi: {2}\nDien tich: {3}".format(self.a,self.b,self.chuvi(),self.dt())
    def chuvi(self):
        return 2*(self.a+self.b)
    def dt(self):
        return self.a*self.b
class hv(hcn):
    def __init__(self, a=0, b=0):
        super().__init__(a, b)
    def chuvihv(self):
        return self.a*4
    def dthv(self):
        return super().dt()
    def __str__(self):
        return super().__str__() + "\nChu vi hv {0}\nDien tich hv: {1}".format(self.chuvihv(),self.dthv())
hv1 = hv(3,3)
print(hv1)'''
class hcn:
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
    def __str__(self):
        return 'Chieu dai: {0}\nChieu rong: {1}\nChu vi: {2}\nDien tich: {3}'.format(self.a,self.b,self.chuvi(),self.dientich())
    def setcanh(self,a=0,b=0):
        self.a=a
        self.b=b
    def getcanh(self):
        return self.a
    def getcanh(self):
        return self.b
    def chuvi(self):
        return 2*(self.a+self.b)
    def dientich(self):
        return self.a*self.b
class hv(hcn):
    def __init__(self, a=0, b=0):
        super().__init__(a, b)
    def chuvihv(self):
        return self.a*4
    def dthv(self):
        return super().dientich()
    def __str__(self):
        return super().__str__() + "\nChu vi hv: {0}\nDien tich hv: {1}".format(self.chuvihv(),self.dthv())
hcn1 = hcn(3,4)
hv1=hv(3,3)
print(hcn1)
print(hv1)