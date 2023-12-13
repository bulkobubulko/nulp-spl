import unittest

class AdditionTestCase(unittest.TestCase):
    """
    A test case class for testing addition, subtraction, multiplication
    and division functions in the calculations module.
    """
    def setUp(self):
        self.calculator = calculations
        self.first_number = 80
        self.second_number = 30
        
    def test_addition(self):
        self.assertEqual(self.calculator.addition(self.first_number, self.second_number), 110)
        self.assertEqual(self.calculator.addition(-self.first_number, -self.second_number), -110)
        
        with self.assertRaises(TypeError):
            self.calculator.addition(f"{self.first_number}", self.second_number)
            self.calculator.addition(f"{self.first_number}", "kachow")
            self.calculator.addition(self.first_number, "kachow")
        
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(self.first_number, self.second_number), 50)
        self.assertEqual(self.calculator.subtraction(self.first_number, -self.second_number), 110)
        
        with self.assertRaises(TypeError):
            self.calculator.subtraction(f"{self.first_number}", self.second_number)
            self.calculator.subtraction(f"{self.first_number}", "kachow")
            self.calculator.subtraction(self.first_number, "kachow")
        
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(self.first_number, self.second_number), 2400)
        self.assertEqual(self.calculator.multiplication(self.first_number, -self.second_number), -2400)
        self.assertEqual(self.calculator.multiplication(0, self.second_number), 0)
        
        with self.assertRaises(TypeError):
            self.calculator.multiplication(f"{self.first_number}", self.second_number)
            self.calculator.multiplication(f"{self.first_number}", "kachow")
            self.calculator.multiplication(self.first_number, "kachow")

    def test_division(self):
        self.assertEqual(self.calculator.division(self.first_number, self.second_number), 2.6666666666666665)
        self.assertEqual(self.calculator.division(self.first_number, -self.second_number), -2.6666666666666665)
        self.assertEqual(self.calculator.division(0, self.second_number), 0)     
               
        with self.assertRaises(TypeError):
            self.calculator.division(f"{self.first_number}", self.second_number)
            self.calculator.division(f"{self.first_number}", "kachow")
            self.calculator.division(self.first_number, "kachow")
        with self.assertRaises(ZeroDivisionError):
            self.calculator.division(self.first_number, 0)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()