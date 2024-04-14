class EuclideanAlgorithm:
    @staticmethod
    def euclidean_algorithm(a, b):
        """
        Computes the greatest common divisor (GCD) of two numbers using the Euclidean Algorithm.

        Args:
            a (int): The first integer.
            b (int): The second integer.
        """
        while b != 0:
            remainder = a % b
            a = b
            b = remainder
        return a  # return int: The greatest common divisor of a and b.

