class Interpolation:
    """
    A class for performing Lagrangian interpolation.
    """

    def __init__(self):
        """
        Initializes an instance of the Interpolation class.
        No specific initialization logic is needed.
        """
        pass

    def lagrangian_interpolation(self, x_array, y_array, x_point):
        """
        Performs Lagrangian interpolation to estimate the y value for a given x point.

        Parameters:
        - x_array (list): List of x values from known data points.
        - y_array (list): List of corresponding y values from known data points.
        - x_point (float): The x value for which the interpolation is needed.

        Returns:
        float: The estimated y value for the given x point.
        """
        x_len = len(x_array)
        y_point = 0

        for i in range(0, x_len):
            p = y_array[i]

            for j in range(0, x_len):
                if i != j:
                    # Lagrange basis polynomial calculation
                    p = p * (x_point - x_array[j]) / (x_array[i] - x_array[j])

            # Accumulate the calculated polynomial term
            y_point = y_point + p

        return y_point


# Example usage
intobj = Interpolation()
result = intobj.lagrangian_interpolation([5, 7, 11, 13, 17], [150, 392, 1452, 2366, 5202], 9)
print(f"The estimated y value for x=9 is: {result}")
