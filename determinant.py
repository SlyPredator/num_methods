from copy import deepcopy

class Determinant:
    """
    A class for computing the determinant of a square matrix using recursive methods.

    Methods
    -------
    processed_matrix(array, k)
        Generates a processed matrix by removing the first row and the k-th column.

    determinant(array)
        Computes the determinant of a square matrix using recursion.
    """

    def __init__(self):
        pass

    def processed_matrix(self, array: list, k: int):
        """
        Generates a processed matrix by removing the first row and the k-th column.

        Parameters
        ----------
        array : list
            The input matrix.
        k : int
            The index of the column to be removed.

        Returns
        -------
        list
            The processed matrix.
        """
        p_matrix = deepcopy(array)
        if len(p_matrix) == 2:
            return p_matrix
        else:
            p_matrix.pop(0)
            for y in p_matrix:
                y.pop(k)
            return p_matrix

    def determinant(self, array: list):
        """
        Computes the determinant of a square matrix using recursion.

        Parameters
        ----------
        array : list
            The input square matrix.

        Returns
        -------
        int or float
            The determinant of the matrix.
        """
        if len(array) == 1:
            det = array[0]
            return det
        elif len(array) == 2:
            det = array[0][0] * array[1][1] - array[1][0] * array[0][1]
            return det
        else:
            det = 0
            for x in range(len(array[0])):
                term = ((-1) ** x) * array[0][x] * self.determinant(self.processed_matrix(array, x))
                det += term
            return det

# Example usage:
detobj = Determinant()
array = [[1, 3, 5], [3, 4, 7], [5, 6, 7]]
print("Determinant is", detobj.determinant(array))
