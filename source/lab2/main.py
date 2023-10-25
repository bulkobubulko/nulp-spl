# Include the parent directory in the system's import path
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

from lab2.calculator import Calculator

def main():
    calcultor = Calculator()
    calcultor.calculate()

if __name__ == "__main__":
    main()