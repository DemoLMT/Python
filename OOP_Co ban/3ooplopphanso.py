class Sophuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def __str__(self):
        a = abs(self.thuc)
        b = abs(self.ao)
        if self.ao > 0:
            return "{0} + {1}i".format(self.thuc, self.ao)
        else:
            return "{0} - {1}i".format(self.thuc, b)

    def __add__(self, sp):
        x = self.thuc + sp.thuc
        y = self.ao + sp.ao
        return Sophuc(x, y)

    def nhan(self, sp):
        x = self.thuc * sp.thuc - self.ao * sp.ao
        y = self.ao * sp.thuc + self.thuc * sp.ao
        return Sophuc(x, y)
if __name__ == '__main__':
    sp1 = Sophuc(1, 2)  # 1+2i
    sp2 = Sophuc(3, 4)  # 3+4i

    print(sp1 + sp2)
    print(sp1.nhan(sp2))