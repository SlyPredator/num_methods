class MatrixOperations:
    """
    A class for performing basic matrix operations: addition, subtraction, and multiplication.
    """

    def __init__(self):
        """
        Initializes an instance of the MatrixOperations class.
        No specific initialization logic is needed.
        """
        pass

    def addition(self, array1, array2):
        """
        Performs matrix addition.

        Parameters:
        - array1 (list): The first matrix.
        - array2 (list): The second matrix.

        Returns:
        list: The result of matrix addition.
        """
        a = len(array1)
        b = len(array1[0])

        result = [[0 for col in range(b)] for row in range(a)]

        for x in range(a):
            for y in range(b):
                # Perform element-wise addition
                result[x][y] += (array1[x][y] + array2[x][y])

        return result

    def subtraction(self, array1, array2):
        """
        Performs matrix subtraction.

        Parameters:
        - array1 (list): The first matrix.
        - array2 (list): The second matrix.

        Returns:
        list: The result of matrix subtraction.
        """
        a = len(array1)
        b = len(array1[0])

        result = [[0 for col in range(b)] for row in range(a)]

        for x in range(a):
            for y in range(b):
                # Perform element-wise subtraction
                result[x][y] += (array1[x][y] - array2[x][y])

        return result

    def multiplication(self, array1, array2):
        """
        Performs matrix multiplication.

        Parameters:
        - array1 (list): The first matrix.
        - array2 (list): The second matrix.

        Returns:
        list: The result of matrix multiplication.
        """
        a = len(array1)
        b = len(array1[0])

        result = [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*array2)] for x_row in array1]

        return result


# Example usage
opobj = MatrixOperations()
p = opobj.multiplication([[10, 9], [8, 7]], [[1, 1], [1, 1]])
print(p)
