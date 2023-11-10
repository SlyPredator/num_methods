class GaussJordan:
    """
    A class for solving a system of linear equations using the Gauss-Jordan elimination method.
    """

    def __init__(self):
        """
        Initializes an instance of the GaussJordan class.
        No specific initialization logic is needed.
        """
        pass

    def gauss_jordan(self, array):
        """
        Solves a system of linear equations using the Gauss-Jordan elimination method.

        Parameters:
        - array (list): A list representing the augmented matrix of the system of linear equations.

        Raises:
        - AssertionError: Raised if a division by zero is encountered during the elimination process.
        """
        n = len(array)
        x = [0] * n

        for i in range(n):
            if array[i][i] == 0.0:
                # If the diagonal element is zero, raise an AssertionError as division by zero is not allowed.
                raise AssertionError("Divide by zero encountered during elimination.")

            for j in range(n):
                if i != j:
                    # Calculate the ratio for row operation
                    ratio = array[j][i] / array[i][i]

                    # Display intermediate steps during the elimination process
                    print(f"Iteration {i} - Row {j} Operation:")
                    print("\n".join([" ".join([str(x) for x in row]) for row in array]))

                    for k in range(n + 1):
                        # Perform row operation to make the element in the current column zero
                        array[j][k] = array[j][k] - ratio * array[i][k]

                        # Display intermediate steps during the row operation
                        print(f"Iteration {i} - Row {j} - Column {k} Operation:")
                        print("\n".join([" | ".join([str(x) for x in row]) for row in array]))

        for i in range(n):
            x[i] = array[i][n] / array[i][i]

        # Display the final solution
        print("\nRequired solution is:")
        for i in range(n):
            print("X%d = %0.2f" % (i, x[i]), end="\t")


# Example usage
array = [[1, -3, -5, -2], [2, -5, -4, 5], [-3, 5, 4, 6]]
obj = GaussJordan()
obj.gauss_jordan(array)
