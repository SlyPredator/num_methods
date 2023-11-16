class RootFinding:
    def __init__(self):
        pass

    def bisection(self, f, a, b, X):
        """
        Find a root of the function within the specified interval using the bisection method.

        Parameters
        ----------
        f : function
            The target function for which the root is to be found.
        a : float/int
            The left endpoint of the interval.
        b : float/int
            The right endpoint of the interval.
        X : int
            The number of iterations to perform.

        Returns
        -------
        float or str
            The approximate root if found within the specified number of iterations,
            or an informative string indicating the outcome.
        """

        if f(a) * f(b) >= 0:
            return "Bisection not possible for this function/values."

        a_new, b_new = a, b

        for n in range(1, X + 1):
            m_new = (a_new + b_new) / 2
            f_m_new = f(m_new)

            if f_m_new == 0:
                return f"Found exact solution at {m_new}"
            elif f(a_new) * f_m_new < 0:
                b_new = m_new
            elif f(b_new) * f_m_new < 0:
                a_new = m_new
            else:
                return "Bisection method failed."
        return (a_new + b_new) / 2

# Example usage
rootobj = RootFinding()
f = lambda x: x**2 - x - 1
print(rootobj.bisection(f, 1, 2, 25))
