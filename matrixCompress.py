import numpy as np

class Approximator:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows, self.cols = self.matrix.shape
        self.row_approx = np.full(self.rows, 1.0)
        self.col_approx = np.full(self.cols, 1.0)


    def itr_reciprocal(self):
        for r in range(self.rows):
            row_reciprocal_sum = np.sum(self.matrix[r, :] / self.col_approx)
            self.row_approx[r] = row_reciprocal_sum / 2

        for c in range(self.cols):
            col_reciprocal_sum = np.sum(self.matrix[:, c] / self.row_approx)
            self.col_approx[c] = col_reciprocal_sum / 2

    def itr_sumdivision(self):
        col_sum = np.sum(self.col_approx)
        self.row_approx = self.matrix.sum(axis=1) / col_sum      
        row_sum = np.sum(self.row_approx)
        self.col_approx = self.matrix.sum(axis=0) / row_sum

        self.matrix = np.outer(self.row_approx, self.col_approx)


    def __str__(self):
        rebuilt_matrix = np.outer(self.row_approx, self.col_approx)
        return str(np.round(rebuilt_matrix, 2))




if __name__ == "__main__":
    matrix = np.array([
        [2, 9, 11],
        [1, 6, 5],
        [8, 4, 2]
    ])

    approximator = Approximator(matrix)
    
    print("Original Matrix:")
    print(approximator.matrix)


    for i in range(5):
        approximator.itr_sumdivision()
        
    print("decomposed vectors : ", approximator.row_approx, "T X", approximator.col_approx)

    print("Approximated matrix")
    print(approximator)
