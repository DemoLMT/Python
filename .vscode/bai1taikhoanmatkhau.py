#cau1
class hv:
    def __init__(self,canh):
        self.canh=canh
    def set_canh(self):
        self.canh=int(self.canh)
    def getcanh(self):
        print(f'Canh : {self.canh}')
    def get_dientich(self):
        dientich=self.canh*self.canh
        print(f'Dien tich : {dientich:.2f}')
hv(2)
hv.getcanh()
hv.get_dientich()