class Matrix:
    def __init__(self, mtrx):
        self.matrix = mtrx
    def __str__(self):
        return '\n'.join((" ".join(str(j) for j in i)) for i in self.matrix)
    def __add__(self, other):
        result = ((self.matrix[i][j] + other.matrix[i][j] 
        for j in range(len(self.matrix[i]))) 
        for i in range(len(self.matrix)))
        return Matrix(result)

first_list = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
second_list = [[4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [1, 2, 3, 4]]
f_l = Matrix(first_list)
s_l = Matrix(second_list)
print(f_l)
print(s_l)
print(f_l + s_l)
