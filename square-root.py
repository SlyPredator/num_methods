class SquareRoot:
    """
    A class for calculating the square root of a number using the iterative method.
    """

    def __init__(self):
        """
        Initializes an instance of the SquareRoot class.
        No specific initialization logic is needed.
        """
        pass

    def square_root(self, n):
        """
        Calculates the square root of a number using the iterative method.

        Parameters:
        - n (float): The number for which the square root is to be calculated.

        Returns:
        float: The square root of the input number.
        """
        y = n
        z = (y + n / y) / 2

        # Iterative method to refine the square root estimate
        while abs(y - z) >= 0.00001:
            # Continue iterating as long as the difference between
            # consecutive square root estimates is greater than or equal to 0.00001.
            y = z
            z = (y + n / y) / 2

        return z


# Example usage
sqobj = SquareRoot()
result = sqobj.square_root(64)
print(result)
