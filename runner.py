# Include the parent directory in the system's import path
import sys
import os

# Get the absolute path to the directory containing runner.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)

# Import main from each lab
from source.lab1 import main as lab1
from source.lab2 import main as lab2
from source.lab3 import main as lab3
from source.lab4 import main as lab4

def main():
    """
    This function is the entry point of the program.
    """
    print(f"Lab1: {lab1.main()}")
    print(f"Lab2: {lab2.main()}")
    print(f"Lab3: {lab3.main()}")
    print(f"Lab4: {lab4.main()}")
     
if __name__ == "__main__":
    main()