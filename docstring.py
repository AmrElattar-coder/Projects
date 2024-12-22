class Calculator:
    """
    A simple calculator class to perform basic operations.
    """

    def add(self, a, b):
        """
        Adds two numbers.
        
        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts the second number from the first.
        
        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The difference between a and b.
        """
        return a - b


calc = Calculator()
print(calc.add(5, 3))   
print(calc.subtract(5, 3))  
