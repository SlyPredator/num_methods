class Factorial:
    """
    A class for calculating the factorial of a number.
    """

    def __init__(self):
        """
        Initializes an instance of the Factorial class.
        No specific initialization logic is needed.
        """
        pass

    def fact1(self, n):
        """
        Calculates the factorial of a given number using recursion.

        Parameters:
        - n (int): The number for which the factorial is to be calculated.

        Returns:
        int: The factorial of the input number.
        """
        # Base case: factorial of 0 is 1
        if n == 0:
            return 1
        # Recursive case: n! = n * (n-1)!
        else:
            return n * self.fact1(n - 1)

# Create an instance of the Factorial class
factobj = Factorial()

# Take user input for the number to calculate the factorial of
user_input = int(input("Enter a number to calculate the factorial of: "))

# Calculate and print the factorial using the fact1 method
result = factobj.fact1(user_input)
print(f"The factorial of {user_input} is: {result}")
