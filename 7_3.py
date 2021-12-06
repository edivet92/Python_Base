class BioCell:
    def __init__(self, cell_amount):
        self.cell_amount = cell_amount
    def make_order(self, row_amount):
        self.row_amount = row_amount
        return "\n".join("*" * self.row_amount 
        for i in range(self.cell_amount//self.row_amount
        )) + '\n' + '*' * (self.cell_amount % self.row_amount) 
    def __str__(self):
        return f'{self.cell_amount}'
    def __add__(self, other):
        return BioCell(self.cell_amount + other.cell_amount)
    def __sub__(self, other):
        return BioCell(self.cell_amount - other.cell_amount) if (self.cell_amount - other.cell_amount) > 0 else 'не получается'
    def __floordiv__(self, other):
        return BioCell(self.cell_amount // other.cell_amount)
    def __mul__(self, other):
        return BioCell(self.cell_amount * other.cell_amount)
pestis = BioCell(17)
choleare = BioCell(13)
print(pestis.make_order(4))
print((pestis + choleare).make_order(5))
print((pestis - choleare).make_order(6))
print((pestis // choleare).make_order(3))
print((pestis * choleare).make_order(9))