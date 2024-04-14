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

if __name__ == "__main__":
    try:
        # Accept input numbers from the user
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        # Calculate the greatest common divisor using Euclidean Algorithm
        gcd = EuclideanAlgorithm.euclidean_algorithm(a, b)

        # Output the result
        print(f"The greatest common divisor of {a} and {b} is {gcd}.")
    except ValueError as e:
        # Handle invalid input
        print(f"Error: {e}")
